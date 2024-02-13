from config import Config
import os
import telebot, requests, random, re 
from telebot import types 

tok = Config.TG_BOT_TOKEN

bot = telebot.TeleBot(tok)
is_bot_active = True  
@bot.message_handler(commands=["start"])
def start(message):
    private = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("✓ تلاوة ", callback_data="quran")
    buttoon = types.InlineKeyboardButton("المصحف", callback_data="starttt")
    butteon = types.InlineKeyboardButton("مطور البوت", url="https://t.me/Almortagel_12")
    private.add(button,buttoon)
    private.add(butteon)   
    bot.send_photo(message.chat.id,"https://t.me/ifuwufuj/29",caption="""
✓ 👋 مرحبا بك عزيزي انا بوت اسلامي اقدم صور دينيه وتلاوات باصوات وابدعات شيوخ متعددين 
لعرض المصحف ارسل رقم الصفحة
✓ 🔍 انقر على الزر ادناة لارسال القران
""", reply_markup=private)
@bot.callback_query_handler(func=lambda call: True)
def tylaoa(call):
    if call.data == "quran":
        voices = "https://t.me/ALMORTAGELRSK/" + str(random.randint(7, 276))
        bot.send_voice(call.message.chat.id, voices, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")



@bot.callback_query_handler(func=lambda call: True)
def imagez(call):
    if call.data == "religious":
        photos = "https://t.me/livequrann/" + str(random.randint(22, 221))
        bot.send_photo(call.message.chat.id, photos, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")

@@bot.callback_query_handler(func=lambda call: True)
def imagezz(call):
    if call.data= "starttt":
    name = message.from_user.first_name
    bot.send_message(message.chat.id,"مرحبا بك في قسم المصحف الرجاء ارسال رقم الصفحة لتصفح صفحات القرآن الكريم للرجوع ارسل /start".format(name))

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
    
    
print("\033[4;35m-"*10)
print("\033[1;33m• Running..... /start ")
print("\033[4;35m-"*10)
bot.polling(none_stop=True)
"""
Dev /- @Almortagel_12
Ch /- @AlmortagelTech
In /- 2024/2/12
"""
