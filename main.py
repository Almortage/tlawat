from config import Config
import os
import telebot, requests, random
from telebot import types 

from config import Config 
import asyncio 
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from kvsqlite.sync import Client as DB
from datetime import date
from pyrogram.errors import FloodWait 
botdb = DB('botdb.sqlite')
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from pyrogram.errors import SessionPasswordNeeded, PhoneCodeExpired
from pyrogram.errors.exceptions.bad_request_400 import PasswordHashInvalid
from pyrogram.errors.exceptions.not_acceptable_406 import PhoneNumberInvalid
from pyrogram.errors.exceptions.bad_request_400 import PhoneCodeInvalid

#حقوق احمد @H1HHIH - @Almortagel_12
# تطوير مودي الهيبه اذا ما ذكرت مصدر بنحكح امك @Almortagel_12 - @SOURCE_ZE 
ownerID = int("5089553588") #ايدي الادمن 
api_hash = Config.API_HASH #ايبي هاش 
api_id = Config.APP_ID #ايبي ايدي
token = Config.TG_BOT_TOKEN #البوت


bot = Client(
  'bot'+token.split(":")[0],
  14911221, #ايبي ايدي
 'a5e14021456afd496e7377331e2e5bcf', #ايبي هاش
  bot_token=token, in_memory=True
)
app = Client(
  name="session",
  api_id=api_id, api_hash=api_hash,
  bot_token=token, in_memory=True
)
#bot = app
#app = bot

STARTKEY = InlineKeyboardMarkup(
       [
         [
           InlineKeyboardButton("≈ إذاعة للمستخدمين ≈", callback_data="broadcast")
         ],
         [
           InlineKeyboardButton("≈ الاحصائيات ≈", callback_data="stats"),
           InlineKeyboardButton("≈ الأدمنية ≈", callback_data="adminstats"),
           InlineKeyboardButton("≈ المحظورين ≈", callback_data="bannedstats"),
         ],
         [
           InlineKeyboardButton("≈ كشف مستخدم ≈",callback_data="whois"),
           InlineKeyboardButton("≈ حظر مستخدم ≈",callback_data="ban"),
         ],
         [
           InlineKeyboardButton("≈ الغاء حظر مستخدم ≈",callback_data="unban"),
         ],
         [
           InlineKeyboardButton("≈ رفع ادمن ≈",callback_data="addadmin"),
           InlineKeyboardButton("≈ تنزيل ادمن ≈",callback_data="remadmin"),
         ]
       ]
     )
if not botdb.get("db"+token.split(":")[0]):
   data = {
     "users":[],
     "admins":[],
     "banned":[],
   }
   botdb.set("db"+token.split(":")[0], data)

if not ownerID in botdb.get("db"+token.split(":")[0])["admins"]:
   data = botdb.get("db"+token.split(":")[0])
   data["admins"].append(ownerID)
   botdb.set("db"+token.split(":")[0], data)

@bot.on_message(filters.command("start") & filters.private)
async def on_start(c,m):
   getDB = botdb.get("db"+token.split(":")[0])
   if m.from_user.id in getDB["banned"]:
     return await message.reply("🚫 تم حظرك من استخدام البوت",quote=True)
   if m.from_user.id == ownerID or m.from_user.id in getDB["admins"]:
     await m.reply(f"**• أهلاً بك ⌯ {m.from_user.mention}\n• إليك لوحة تحكم الادمن**",reply_markup=STARTKEY,quote=True)
   if not m.from_user.id in getDB["users"]:
      data = getDB
      data["users"].append(m.from_user.id)
      botdb.set("db"+token.split(":")[0], data)
      for admin in data["admins"]:
         text = f"– New user stats the bot :"
         username = "@"+m.from_user.username if m.from_user.username else "None"
         text += f"\n\n𖡋 𝐔𝐒𝐄 ⌯  {username}"
         text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {m.from_user.mention}"
         text += f"\n𖡋 𝐈𝐃 ⌯  `{m.from_user.id}`"
         text += f"\n𖡋 𝐃𝐀𝐓𝐄 ⌯  **{date.today()}**"
         try: await c.send_message(admin, text, reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton (m.from_user.first_name,user_id=m.from_user.id)]]))
         except: pass
   data = {"name":m.from_user.first_name[:25], "username":m.from_user.username, "mention":m.from_user.mention(m.from_user.first_name[:25]),"id":m.from_user.id}
   botdb.set(f"USER:{m.from_user.id}",data)


@bot.on_message(filters.private & ~filters.service)
async def on_messages(c,m):       
   if botdb.get(f"broad:{m.from_user.id}") and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      text = "**— جاري إرسال الإذاعة إلى المستخدمين**\n"
      reply = await m.reply(text,quote=True)
      count=0
      users=botdb.get("db"+token.split(":")[0])["users"]
      for user in users:
        try:
          await m.copy(user)
          count+=1
          await reply.edit(text+f"**— تم ارسال الإذاعة الى [ {count}/{len(users)} ] مستخدم**")
        except FloodWait as x:
          await asyncio.sleep(x.value)
        except Exception:
          pass
      return True
   
   if m.text and botdb.get(f"whois:{m.from_user.id}") and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
         name=getUser["name"]
         id=getUser["id"]
         mention=getUser["mention"]
         username="@"+getUser["username"] if getUser["username"] else "None"
         language=botdb.get(f"LANG:{id}")
         text = f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
         text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
         text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
         text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
         text += f"\n𖡋 𝐀𝐂𝐂 𝑳𝐈𝐍𝐊 ⌯  **{mention}**"
         return await m.reply(text,quote=True)
   
   if m.text and botdb.get(f"ban:{m.from_user.id}") and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
        if getUser["id"] in botdb.get("db"+token.split(":")[0])["admins"]:
          return await m.reply(f"– لا يمكنك حظر ⌯ {getUser['mention']} ⌯ لأنه ادمن",quote=True)
        else:
          if getUser["id"] in botdb.get("db"+token.split(":")[0])["banned"]:
            return await m.reply(f"– لا يمكنك حظر ⌯ {getUser['mention']} ⌯ لأنه محظور مسبقاً",quote=True)
          name=getUser["mention"]
          id=getUser["id"]
          username="@"+getUser["username"] if getUser["username"] else "None"
          language=botdb.get(f"LANG:{id}")
          text = f"- This user added to blacklist:\n\n"
          text += f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
          text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
          text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
          text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
          data = botdb.get("db"+token.split(":")[0])
          data["banned"].append(id)
          botdb.set("db"+token.split(":")[0],data)
          return await m.reply(text,quote=True)
   
   if m.text and botdb.get(f"unban:{m.from_user.id}") and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
        if getUser["id"] in botdb.get("db"+token.split(":")[0])["admins"]:
          return await m.reply(f"– لا يمكنك الغاء حظر ⌯ {getUser['mention']} ⌯ لأنه ادمن",quote=True)
        else:
          if not getUser["id"] in botdb.get("db"+token.split(":")[0])["banned"]:
            return await m.reply(f"– لا يمكنك الغاء حظر ⌯ {getUser['mention']} ⌯ لأنه غير محظور مسبقاً",quote=True)
          name=getUser["mention"]
          id=getUser["id"]
          username="@"+getUser["username"] if getUser["username"] else "None"
          language=botdb.get(f"LANG:{id}")
          text = f"- This user deleted from blacklist:\n\n"
          text += f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
          text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
          text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
          text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
          data = botdb.get("db"+token.split(":")[0])
          data["banned"].remove(id)
          botdb.set("db"+token.split(":")[0],data)
          return await m.reply(text,quote=True)
   
   if m.text and botdb.get(f"add:{m.from_user.id}") and m.from_user.id == ownerID:
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
        if getUser["id"] in botdb.get("db"+token.split(":")[0])["admins"]:
          return await m.reply(f"– لا يمكنك رفع ⌯ {getUser['mention']} ⌯ لأنه ادمن مسبقاً",quote=True)
        if getUser["id"] in botdb.get("db"+token.split(":")[0])["banned"]:
          return await m.reply(f"– لا يمكنك رفع ⌯ {getUser['mention']} ⌯ لأنه محظور",quote=True)
        else:          
          name=getUser["mention"]
          id=getUser["id"]
          username="@"+getUser["username"] if getUser["username"] else "None"
          language=botdb.get(f"LANG:{id}")
          text = f"- This user added to admins list:\n\n"
          text += f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
          text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
          text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
          text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
          data = botdb.get("db"+token.split(":")[0])
          data["admins"].append(id)
          botdb.set("db"+token.split(":")[0],data)
          return await m.reply(text,quote=True)
   
   if m.text and botdb.get(f"rem:{m.from_user.id}") and m.from_user.id == ownerID:
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      getUser=botdb.get(f"USER:{m.text[:15]}")
      if not getUser:
        return await m.reply("– لا يوجد مستخدم بهذا الآيدي",quote=True)
      else:
        if not getUser["id"] in botdb.get("db"+token.split(":")[0])["admins"]:
          return await m.reply(f"– لا يمكنك تنزيل ⌯ {getUser['mention']} ⌯ لأنه مو ادمن",quote=True)
        if getUser["id"] == ownerID:
          return await m.reply(f"– لا يمكنك تنزيل ⌯ {getUser['mention']} ⌯ لأنه مالك البوت",quote=True)
        else:
          name=getUser["mention"]
          id=getUser["id"]
          username="@"+getUser["username"] if getUser["username"] else "None"
          language=botdb.get(f"LANG:{id}")
          text = f"- This user deleted from admins list:\n\n"
          text += f"𖡋 𝐔𝐒𝐄 ⌯  {username}"
          text += f"\n𖡋 𝐍𝐀𝐌𝐄 ⌯  {name}"
          text += f"\n𖡋 𝑳𝐀𝐍𝐆 ⌯  {language}"
          text += f"\n𖡋 𝐈𝐃 ⌯  `{id}`"
          data = botdb.get("db"+token.split(":")[0])
          data["admins"].remove(id)
          botdb.set("db"+token.split(":")[0],data)
          return await m.reply(text,quote=True)

@bot.on_callback_query()
async def on_Callback(c,m):      
   if m.data == "broadcast" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      await m.edit_message_text("• أرسل الإذاعة الآن ( صورة ، نص ، ملصق ، ملف ، صوت )\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"broad:{m.from_user.id}",True)
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      
   if m.data == "whois" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      await m.edit_message_text("• ارسل الآن ايدي المستخدم للكشف عنه\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"whois:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      
   if m.data == "ban" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      await m.edit_message_text("• ارسل الآن ايدي المستخدم لحظره\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"ban:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
   
   if m.data == "unban" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      await m.edit_message_text("• ارسل الآن ايدي المستخدم لرفع حظره\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"unban:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
   
   if m.data == "addadmin" and m.from_user.id == ownerID:
      await m.edit_message_text("• ارسل الآن ايدي المستخدم لرفعه ادمن\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"add:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
   
   if m.data == "remadmin" and m.from_user.id == ownerID:
      await m.edit_message_text("• ارسل الآن ايدي المستخدم لرفعه ادمن\n• للإلغاء ارسل الغاء ",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("رجوع",callback_data="back")]]))
      botdb.set(f"rem:{m.from_user.id}",True)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")

   if m.data == "back" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      #await m.answer("• تم الرجوع بنجاح والغاء كل شي ",show_alert=True)
      await m.edit_message_text(f"**• أهلاً بك ⌯ {m.from_user.mention}\n• إليك لوحة تحكم الادمن**",reply_markup=STARTKEY)
      botdb.delete(f"broad:{m.from_user.id}")
      botdb.delete(f"whois:{m.from_user.id}")
      botdb.delete(f"ban:{m.from_user.id}")
      botdb.delete(f"add:{m.from_user.id}")
      botdb.delete(f"rem:{m.from_user.id}")
      botdb.delete(f"unban:{m.from_user.id}")
      
   if m.data == "stats" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      users = len(botdb.get("db"+token.split(":")[0])["users"])
      await m.answer(f"• احصائيات البوت ⌯ {users}", show_alert=True,cache_time=10)
      
   if m.data == "adminstats" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      admins = len(botdb.get("db"+token.split(":")[0])["admins"])
      await m.answer(f"• احصائيات الادمنية ⌯ {admins}\n• سيتم ارسال بيانات كل آدمن", show_alert=True,cache_time=60)
      text = "- الادمنية:\n\n"
      count = 1
      for admin in botdb.get("db"+token.split(":")[0])["admins"]:
         if count==101: break
         getUser = botdb.get(f"USER:{admin}")
         mention=getUser["mention"]
         id=getUser["id"]
         text += f"{count}) {mention} ~ (`{id}`)\n"
         count+=1
      text+="\n\n—"
      await m.message.reply(text,quote=True)
   
   if m.data == "bannedstats" and (m.from_user.id == ownerID or m.from_user.id in botdb.get("db"+token.split(":")[0])["admins"]):
      bans = botdb.get("db"+token.split(":")[0])["banned"]
      if not bans:  return await m.answer("• لا يوجد محظورين", show_alert=True,cache_time=60)
      await m.answer(f"• احصائيات المحظورين ⌯ {len(bans)}\n• سيتم ارسال بيانات كل المحظورين", show_alert=True,cache_time=60)
      text = "- المحظورين:\n\n"
      count = 1
      for banned in bans:
         if count==101: break
         getUser = botdb.get(f"USER:{banned}")
         mention=getUser["mention"]
         id=getUser["id"]
         text += f"{count}) {mention} ~ (`{id}`)\n"
         count+=1
      text+="\n\n—"
      await m.message.reply(text,quote=True)
@bot.message_handler(commands=["start"])
def start(message):
    private = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("كتب دينية ", callback_data="quran")
    butteon = types.InlineKeyboardButton("مطور البوت", url="https://t.me/Almortagel_12")
    buttoon = types.InlineKeyboardButton("قناة البوت", url="https://t.me/AlmortagelTech")
    private.add(button)
    private.add(butteon,buttoon)   
    bot.send_photo(message.chat.id,"https://t.me/ifuwufuj/29",caption="""
✓ 👋 مرحبا بك عزيزي انا بوت اسلامي اقدم صور دينيه وتلاوات باصوات وابدعات شيوخ متعددين 
لعرض المصحف ارسل رقم الصفحة
✓ 🔍 انقر على الزر ادناة لارسال القران
""", reply_markup=private)
@bot.callback_query_handler(func=lambda call: True)
def tylaoa(call):
    if call.data == "quran":
        voices = "https://t.me/kotobeslameah/" + str(random.randint(2, 2020))
        bot.send_pdf(call.message.chat.id, voices, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
@bot.callback_query_handler(func=lambda call: True)
def tylaoa(call):
    if call.data == "kottab":
        voicess = "https://t.me/telawatnader/" + str(random.randint(7, 265))
    bot.send_voice(call.message.chat.id, voicess, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
@bot.callback_query_handler(func=lambda call: True)
def tylaoa(call):
    if call.data == "nqsbndy":
        voicesss = "https://t.me/ggcnjj/" + str(random.randint(2, 114))
        bot.send_voice(call.message.chat.id, voicesss, caption="""ابتهلات الشيخ نقشبندي""")

@bot.callback_query_handler(func=lambda call: True)
def starttt(call):
    if call.data == "starttt":
       bot.send_message(message.chat.id,caption="""
مرحبا بك في قسم المصحف الرجاء ارسال رقم الصفحة لتصفح صفحات القرآن الكريم للرجوع ارسل /start
""")

@bot.message_handler(func=lambda message: True)
def all(message):
    try:
            num = int(message.text)
            url = "https://quran.ksu.edu.sa/png_big/" + str(num) + ".png"

            keyboard = types.InlineKeyboardMarkup()
            cou = types.InlineKeyboardButton(text=f"• {num} •", callback_data="couu")
            previous = types.InlineKeyboardButton(text="صفحة السابقة", callback_data=str(num - 1))
            next = types.InlineKeyboardButton(text="صفحة التالية", callback_data=str(num + 1))

            keyboard.row(cou)
            keyboard.row(previous,next)

            bot.send_photo(message.chat.id,url, reply_markup=keyboard)
    except:
            pass
            bot.reply_to(message,'error')

@bot.callback_query_handler(func=lambda call: True)
def alll(call):
    if call.data == 'couu':
     bot.answer_callback_query(call.id, text='هذا زر يعرض فيه العدد فقط')
     exit()
    num = int(call.data)
    url = "https://quran.ksu.edu.sa/png_big/" + str(num) + ".png"

    keyboard = types.InlineKeyboardMarkup()

    cou = types.InlineKeyboardButton(text=f"• {num} •", callback_data="couu")
    previous = types.InlineKeyboardButton(text="صفحة السابقة", callback_data=str(num - 1))
    next = types.InlineKeyboardButton(text="صفحة التالية", callback_data=str(num + 1))


    keyboard.row(cou)
    keyboard.row(previous,next)

    bot.edit_message_media(types.InputMediaPhoto(url), call.message.chat.id, call.message.message_id,reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def msgs(message):
    text = message.text
    if text == "عبدالباسط" or date == "nkssd":
        voice_url = "https://t.me/telawatnader/" + str(random.randint(7, 265))
        bot.send_voice(message.chat.id, voice_url, caption="🥹♥ ¦ تـم اختيـار الشيخ عبدالباسط لـك")
            
print("تم تشغيل البوت اذا وقف معك شي تواصل معي @Almortagel_12")
bot.polling(none_stop=True)
"""
Dev /- @Almortagel_12
Ch /- @AlmortagelTech
In /- 2024/2/14
"""