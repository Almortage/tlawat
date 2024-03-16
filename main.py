import telebot
from telebot import types
import os
from config import Config

id = 5089553588
bot_token = Config.TG_BOT_TOKEN
bot = telebot.TeleBot(bot_token) 

ch = "-1001287057545" # ايدي قناتك هنا لاتمسح -100
t = ['creator', 'member', 'administrator']
use = "AlmortagelTech"

@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.type == 'private':
        user_id = str(message.from_user.id)        
        with open("ids.txt", 'a+') as file:
            file.seek(0)          
            if user_id not in file.read():
                file.write(user_id + '\n')

    if bot.get_chat_member(chat_id=ch, user_id=message.from_user.id).status not in t:
        
        bot.reply_to(message, "عذرا عزيزي المستخدم ، \n عليك الاشتراك بقنوات البوت لتتمكن من استخدامة [ {}] \n- - - - - - - - - - \n اشترك من ثم ارسل /start".format(use))
        return            
    idu = message.from_user.id
    tnt = types.InlineKeyboardMarkup(row_width=1)
    s1 = types.InlineKeyboardButton("تلاوات دينية" , callback_data="quran")
    s2 = types.InlineKeyboardButton("صور دينيه" , callback_data="religious")
    tnt.add(s1,s2)
    bot.reply_to(message, f"مرحبا صديقي  [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n البوت يحتوي على تلاوات  وصور دينية استخدم الي يناسبك من الازرار 👇",parse_mode="markdown",reply_markup=tnt)
    
    if idu == id:
        but = types.InlineKeyboardMarkup(row_width=1)
        a2 = types.InlineKeyboardButton("اذاعة", callback_data="all")
        a3 = types.InlineKeyboardButton("ارسل التخزين", callback_data="send_file")
        but.add(a2)
        but.add(a3)
        bot.reply_to(message, "مرحبا عزيزي المطور \n هذه هي لوحة التحكم الخاصة بك\n اذا تريد تعرف احصائيات البوت ارسل /stats", reply_markup=but) 
               
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
        voices = "https://t.me/livequrann/" + str(random.randint(7, 276))
        bot.send_photo(call.message.chat.id, voices, caption="""
✓ تم اختيار صوره دينية لك""")       		
@bot.message_handler(commands=["stats"])
def stats(message):
    if message.from_user.id == id:  # تأكد أن معرف المرسل هو معرف المطور المخول
        with open("ids.txt") as file:
            lines = file.readlines()
            # تصفية الأسطر الفارغة والتي تحتوي على مسافات بيضاء
            clean_lines = [line.strip() for line in lines if line.strip()]
            num_users = len(clean_lines)
        bot.reply_to(message, f"عدد أعضاء البوت: {num_users}")


##############################

@bot.callback_query_handler(func=lambda call: True)
def calldata(call):
    if call.data == "send_file":
        with open("ids.txt", "r") as file:
            bot.send_document(call.message.chat.id, file)
    elif call.data == "all":
        bot.send_message(call.message.chat.id, "• ارسل الان ماتريد إذاعته • \n نص - صورة - ملف")
        bot.register_next_step_handler(call.message, send_broadcast_message)

def send_broadcast_message(message):
    with open("ids.txt", "r") as file:
        user_ids = file.readlines()
        for user_id in user_ids:
            if message.text:
                bot.send_message(user_id.strip(), text=message.text)
            elif message.photo:
                bot.send_photo(user_id.strip(), photo=message.photo[-1].file_id, caption=message.caption)
            elif message.document:
                bot.send_document(user_id.strip(), data=message.document.file_id, caption=message.caption, parse_mode='Markdown')
# @world_father
# @world_father
@bot.callback_query_handler(func=lambda call: True)
def calldata(call):
    if call.data == "send_file":
        with open("ids.txt", "r") as file:
            bot.send_document(call.message.chat.id, file)

print("تم تشغيل البوت بواسطة المرتجل=")
bot.polling()
