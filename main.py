import requests, threading, time, random, json, os
from telebot import TeleBot 
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton,  CallbackQuery

# api الإذكار
url = "https://hmsbots.aba.vg/apieati/ApiAthkar.php"


bot_token = Config.TG_BOT_TOKEN
developer = 5089553588


app = TeleBot(bot_token)

# ضيف صلوات اكتر.
salat_nabi = [
    "اَللَّهُمَّ صَلَّي وَسَلَّمَ وَبَارَكَ عَلَى سَيِّدِنَا مُحَمَّدْ وَعَلَى آلِهِ وَصَحْبِهِ وَسَلَّمَ تَسْلِيمًا كَثِيرًا",
    "صَلَوَات اَللَّهِ عَلَيْكَ يَاحَبِيبِي يَارْسُولْ اَللَّهِ",
    "صَلَّي عَلَى سَيِّدِنَا مُحَمَّدْ خَيْرْ اَلْأَنَامِ",
    "قَالَ رسُولُ اللَّهِ ﷺ: الْبخِيلُ مَنْ ذُكِرْتُ عِنْدَهُ، فَلَم يُصَلِّ علَيَّ\n\nصَلَّى اَللَّهُ عَلَيْهِ وَسَلَّمَ"
]

@app.message_handler(commands=["start"], chat_types=["private"])
def start(message: Message):
    bot_info = app.get_me()
    dev_info = app.get_chat(developer)
    bot_user = bot_info.username
    user_id = message.from_user.id
    if user_id not in list(users.keys()):
        users[str(user_id)] = {
            "prophet" : False,
            "azkar" : False
        }
        write(db_path, users)
    caption = f"""🙋🏻‍♂️︙مرحباً عزيزي {message.from_user.first_name}
   
🤖 ⌯ هذا البوت مخصص لنشر أدعية وأذكار وأيضا الصلاةعلى النبي كل ساعة للقنوات والمجموعات.
🎛️ ⌯ إضغط على تعليمات لتلقي الأوامر.

⬇️ ⌯ قم بالتحكم بالبوت الان بواسطة الازرار بالأسفل.
"""
    markup = [
        [
            InlineKeyboardButton("تعليمات", callback_data="help")
        ],
        [
            InlineKeyboardButton("اضافة البوت لقناه 🤖", f"http://t.me/{bot_user}?startchannel=new"),
            InlineKeyboardButton("إضافة البوت لمجموعه 🤖", f"http://t.me/{bot_user}?startgroup=true")            
        ],
        [
            InlineKeyboardButton(dev_info.first_name, f"https://t.me/{dev_info.username}")
        ]
    ]
    app.reply_to(
        message,
       text=caption,
       reply_markup=InlineKeyboardMarkup(markup)
   )

@app.message_handler(commands=["private_azkar"], chat_types=["private"])
@app.message_handler(func=lambda message: message.text == "تفعيل الاذكار", chat_types=["group",  "channel"])
def enable_azkar(message: Message):
    chat_id = message.chat.id
    if chat_id not in list(users.keys()):
        users[str(chat_id)] = {
            "prophet" : False,
            "azkar" : True
        }
        write(db_path, users)
        app.reply_to(message, "تم تفعيل الأذكار و الأدعيه 💙!️")
        return
    elif chat_id in list(users.keys()) and not users[chat_id]["azkar"]:
        users[str(chat_id)]["azkar"] = True
        app.reply_to(message, "تم تفعيل الأذكار و الأدعيه 💙!️")
    app.reply_to(message, "الأذكار والأدعيه مفعله 💙!")

@app.message_handler(commands=["cancel_azkar"], chat_types=["private"])
@app.message_handler(func=lambda message: message.text == "تعطيل الاذكار", chat_types=["group",  "channel"])
def disable_azkar(message: Message):
    chat_id = message.chat.id
    if chat_id in list(users.keys()) and users[chat_id]["azkar"]:
        users[str(chat_id)]["azkar"] = False
        write(db_path, users)
        app.reply_to(message, "تم تعطيل الأذكار و الأدعيه 🥲!\n\nترفض الحسنات؟ 🥲!️")
        return
    app.reply_to(message, "الأذكار والأدعيه غير مفعله 🥲")
 
@app.message_handler(commands=["private_prophet"], chat_types=["private"])
@app.message_handler(func=lambda message: message.text == "تفعيل الصلاه على النبي", chat_types=["group",  "channel"])
def enable_nabi(message: Message):
    chat_id = message.chat.id
    if chat_id not in list(users.keys()):
        users[str(chat_id)] = {
            "prophet" : True,
            "azkar" : False
        }
        write(db_path, users)
        app.reply_to(message, "تم تفعيل الصلاه على النبي 💙!\n\nعليه أفضل الصلاه و أتم التسليم ❤️❤️")
        return
    elif chat_id in list(users.keys()) and not users[chat_id]["prophet"]:
        users[str(chat_id)]["prophet"] = True
        write(db_path, users)
        app.reply_to(message, "تم تفعيل الصلاه على النبي 💙!\n\nعليه أفضل الصلاه و أتم التسليم ❤️❤️")
        return
    app.reply_to(message, "الصلاه على النبي مفعله 💙")

@app.message_handler(commands=["cancel_prophet"], chat_types=["private"])
@app.message_handler(func=lambda message: message.text == "تعطيل الصلاه على النبي", chat_types=["group",  "channel"])
def disable_nabi(message: Message):
    chat_id = message.chat.id
    if chat_id in list(users.keys()) and users[chat_id]["prophet"]:
        users[str(chat_id)]["prophet"] = False
        write(db_path, users)
        app.reply_to(message, "تم تعطيل الصلاه على النبي 🥲\n\nترفض الحسنات؟ 🥲")
        return
    app.reply_to(message, "الصلاه على النبي غير مفعله 🥲")


@app.callback_query_handler(func=lambda callback: callback.data == "help")
def help(callback: CallbackQuery):
    caption = """🎛️︙التعليمات :

⬆️ ⌯ كيفية جعل البوت يرسل الأذكار !؟.

✳️︙أضف البوت الى قناتك أو مجموعتك وقم برفعه مشرف.

✳️︙للتفعيل في المجموعات/القنوات أرسل في المجموعة/القناه كلمة تفعيل

✳️︙يمكنك جعل البوت أيضاً يرسل الأذكار لك على الخاص بالضغط على /private_azkar لتفعيل الأذكار والادعيه و /private_prophet لتفعيل الصلاه على النبي 


⬇️ ⌯ كيفية إيقاف البوت من إرسال الأذكار !؟.

⛔︙لإيقاف البوت من إرسال الأذكار/الصلاه على النبي لك على الخاص إضغط على : /cancel_azkar | /cancel_prophet
"""
    markup = [
        [
            InlineKeyboardButton("العوده 🔙", callback_data="main")
        ]
    ]
    
    app.edit_message_text(
        message_id=callback.message.id,
        chat_id=callback.from_user.id, 
        text=caption,
        reply_markup=InlineKeyboardMarkup(markup) 
    )

@app.callback_query_handler(func=lambda callback: callback.data == "main")
def restart(callback: CallbackQuery):
    bot_info = app.get_me()
    dev_info = app.get_chat(developer)
    bot_user = bot_info.username
    user_id = callback.from_user.id
    caption = f"""🙋🏻‍♂️︙مرحباً عزيزي {callback.from_user.first_name}
   
🤖 ⌯ هذا البوت مخصص لنشر أدعية وأذكار وأيضا الصلاةعلى النبي كل ساعة للقنوات والمجموعات.
🎛️ ⌯ إضغط على تعليمات لتلقي الأوامر.

⬇️ ⌯ قم بالتحكم بالبوت الان بواسطة الازرار بالأسفل.
"""
    markup = [
        [
            InlineKeyboardButton("تعليمات", callback_data="help")
        ],
        [
            InlineKeyboardButton("اضافة البوت لقناه 🤖", f"http://t.me/{bot_user}?startchannel=new"),
            InlineKeyboardButton("إضافة البوت لمجموعه 🤖", callback_data=f" http://t.me/{bot_user}?startgroup")
        ],
        [
            InlineKeyboardButton(dev_info.first_name, f"https://t.me/{dev_info.username}")
        ]
    ]
    app.edit_message_text(
        message_id=callback.message.id, 
        chat_id=callback.message.chat.id, 
        text=caption,
        reply_markup=InlineKeyboardMarkup(markup)
    )
    
    
def main():
    azkar_thread = threading.Thread(target=azkar)
    prophet_thread = threading.Thread(target=prophet)
    azkar_thread.start()
    prophet_thread.start()
    
    
def azkar():
    while True:
        if len(list(users.keys())) == 0:
            continue
        response = requests.get(url).text
        for user in users.keys():
            if users[user].get("azkar"):
                try:
                    app.send_message(
                        user,
                        response
                    )
                except:
                    continue
            continue
        time.sleep(60)

def prophet():
    while True:
        if len(list(users.keys())) == 0:
            continue
        choice = random.choice(salat_nabi)
        for user in users.keys():
            if users[user].get("prophet"):
                try:
                    app.send_message(
                        user,
                        choice
                    )
                except:
                    continue
            continue
        time.sleep(60)

def write(file_path, data):
    with open(file_path, "w") as jsonfile:
        json.dump(data, jsonfile, indent=2)
        
def read(file_path):
    with open(file_path, "r") as jsonfile:
        return json.load(jsonfile)

if __name__ == "__main__":
    db_path = "users.json"
    if not os.path.exists(db_path):
        write(db_path, {})
    users = read(db_path)
    thread = threading.Thread(target=main)
    thread.start()
    app.infinity_polling()