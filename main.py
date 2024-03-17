import telebot, requests, random, re 
from config import Config
from telebot import types 
import os

id = 5089553588
token = Config.TG_BOT_TOKEN#توكنك
bot = telebot.TeleBot(token)   
@bot.message_handler(commands=["start"])
def start(message):
    private = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("✓ تلاوة ", callback_data="quran")
    buttoon = types.InlineKeyboardButton("✓ صورة دينية ", callback_data="religious")
    buttn = types.InlineKeyboardButton("خطب دينيه", callback_data="quraan")
    buttin = types.InlineKeyboardButton("الصلي علي النبي", callback_data="qurn")
    bstart = types.InlineKeyboardButton("المصحف", callback_data="starttt")
    butin = types.InlineKeyboardButton("احاديث دينية", callback_data="religiou")
    bkotob = types.InlineKeyboardButton("كتب دينية", callback_data="kotob")
    buttooon = types.InlineKeyboardButton("المطور", url= "https://t.me/Almortagel_12")
    private.add(button,buttoon)
    private.add(buttin,buttn)
    private.add(bstart,butin)
    private.add(bkotob)
    private.add(buttooon)    
    bot.send_photo(message.chat.id,"https://t.me/ifuwufuj/29",caption="""
✓ 👋 مرحبا بك عزيزي في انا بوت  اسلامي اقدم تلاوات باصوات وابدعات شيوخ متعددين 
✓ 🔍 انقر على الزر ادناة لارسال ماتريد
""", reply_markup=private)
@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.type == 'private':
        user_id = str(message.from_user.id)        
        with open("ids.txt", 'a+') as file:
            file.seek(0)          
            if user_id not in file.read():
                file.write(user_id + '\n')
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
    elif call.data == "religious":
        voicees = "https://t.me/livequrann/" + str(random.randint(22, 221))
        bot.send_photo(call.message.chat.id, voicees, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
    elif call.data == "quraan":
        voicess = "https://t.me/fresdewi/" + str(random.randint(2, 201))
        bot.send_voice(call.message.chat.id, voicess, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
    elif call.data == "religiou":
        voice = "https://t.me/dmatrix12/" + str(random.randint(799, 1341))
        bot.send_photo(call.message.chat.id, voice, caption="""
✓  🌿 〈〈 صـل على سيدنا محمد 〉〉
""")
    elif call.data == "kotob":
        voic = "https://t.me/kotobeslameah/" + str(random.randint(2, 1950))
        bot.send_document(call.message.chat.id, voic, caption="""
 تم اختيار هذا الكتاب لك
""")
    elif call.data == "qurn":
        voics = ["اللهم صلي علي سيدنا ونبينا محمد",]
        bot.send_message(call.message.chat.id, voics)
    elif call.data == "starttt":
        voic = ["مرحبا بك في قسم المصحف الرجاء ارسال رقم الصفحة لتصفح صفحات القرآن الكريم للرجوع ارسل /start",]
        bot.send_message(call.message.chat.id,voic)

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
    

t = ['creator', 'member', 'administrator']
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

print("@Almortagel_12")
print("\033[1;33m• Running..... /start ")
bot.polling(none_stop=True)
