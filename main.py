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
    buttoon = types.InlineKeyboardButton("✓ صورة دينية ", callback_data="religious")
    private.add(buttoon)
    private.add(button)   
    bot.send_photo(message.chat.id,"https://t.me/ifuwufuj/29",caption="""
✓ 👋 مرحبا بك عزيزي انا بوت اسلامي اقدم صور دينيه وتلاوات باصوات وابدعات شيوخ متعددين 
✓ 🔍 انقر على الزر ادناة لارسال تلاوة
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
print("\033[4;35m-"*10)
print("\033[1;33m• Running..... /start ")
print("\033[4;35m-"*10)
bot.polling(none_stop=True)
"""
Dev /- @Almortagel_12
Ch /- @AlmortagelTech
In /- 2024/2/12
"""
