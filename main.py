import telebot, requests, random, re 
from config import Config
from telebot import types 
import os

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
    bstarjt = types.InlineKeyboardButton(" اوقات الصلاة", callback_data="starjt")
    buttooon = types.InlineKeyboardButton("المطور", url= "https://t.me/Almortagel_12")
    private.add(button,buttoon)
    private.add(buttin,buttn)
    private.add(bstart,butin)
    private.add(bkotob,bstarjt)
    private.add(buttooon)    
    bot.send_photo(message.chat.id,"https://t.me/ifuwufuj/29",caption="""
✓ 👋 مرحبا بك عزيزي في انا بوت  اسلامي اقدم تلاوات باصوات وابدعات شيوخ متعددين 
✓ 🔍 انقر على الزر ادناة لارسال ماتريد
""", reply_markup=private)
        
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
@bot.callback_query_handler(func=lambda call: True)
def tylaoa(call):
    if call.data == "starjt":
        voict = ["اهلا بك عزيزي في قسم مواقيت الصلاة انتظر ارسل اسم مدينتك او دولتك لاقوم بجلب اوقات الصلاة بأسم مدينك او بأسم دولتك",]
        bot.send_message(call.message.chat.id,voict)
@bot.message_handler(content_types=['text'])
def timings(message):
	brok = bot.reply_to(message,'حسناا انتظر ')
	try:
		msg = message.text
		response = requests.get(f'https://timesprayer.com/prayer-times-in-{msg}.html').text
		ggg = re.search("<title>(.*?)</title>",response).group(1)
		fajr = re.search("<td><strong>صلاة الفجْر</strong></td><td>(.*?)</td></tr>", response).group(1);alshuruq = re.search("<td><strong> الشروق</strong></td><td>(.*?)</td></tr>", response).group(1);alzuhr = re.search("<td><strong>صلاة الظُّهْر</strong></td><td>(.*?)</td></tr>", response).group(1);aleasr = re.search("<td><strong>صلاة العَصر</strong></td><td>(.*?)</td></tr>", response).group(1);almaghrib = re.search("<td><strong>صلاة المَغرب</strong></td><td>(.*?)</td></tr>", response).group(1);aleisha = re.search("<td><strong>صلاة العِشاء</strong></td><td>(.*?)</td></tr>", response).group(1)
		
		almakan = re.search("<div><b>المكان :</b> (.*?)</div>",response).group(1)
		
		alsala = re.search("<div><b>الصلاة القادمة :</b> (.*?)</div>",response).group(1)
		
		saea = re.search("<div><b>ساعات الصيام :</b> (.*?)</div>",response).group(1)
		
		miladi = re.search("<div><b>التاريخ :</b> (.*?)</div>",response).group(1)
		
		hijri = re.search("<div><b>هجري :</b> (.*?)</div>",response).group(1)
		
		day = re.search("<b>اليوم :</b> (.*?)</div>",response).group(1)
		
		tim = re.search('<b id="timenowinthecity">(.*?)</b>',response).group(1)
		
		alzamania = re.search('(?<=title=")(\w+/\w+)', response).group(1)
		
		name = ggg.split("في")[1].strip()
		text = f"{ggg}\n\nصلاة الفجر: {fajr}\nالشروق: {alshuruq}\nصلاة الظهر: {alzuhr}\nصلاة العصر: {aleasr}\nصلاة المغرب: {almaghrib}\nصلاة العشاء: {aleisha}\n — — — — — —\nالمكان: {almakan}\nالصلاة القادمة: {alsala}\nساعات الصيام: {saea}\nالتاريخ: {miladi}\nهجري: {hijri}\nالوقت الان: {tim} حسب التوقيت المحلي في {name}\nاليوم: {day}\nالمنطقة الزمنية: {alzamania}"
		bot.delete_message(message.chat.id,message_id=brok.message_id)
		bot.reply_to(message,text)
		
	except:
		bot.edit_message_text(chat_id=message.chat.id, message_id=brok.message_id, text='لم اتعرف على اسم المدينة')
print("@Almortagel_12")
print("\033[1;33m• Running..... /start ")
bot.polling(none_stop=True)
