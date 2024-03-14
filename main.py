from config import Config
import os
import random
import requests
import telebot
from telebot import types
linksramdan = 'https://i.ibb.co/ThYVFLf/bda625a868b0.jpg','https://i.ibb.co/fQqYFt3/e896c04e74ff.jpg','https://i.ibb.co/HXPVRkF/dcea9320292d.jpg','https://i.ibb.co/FsCS00H/d18d4ad3684d.jpg','https://i.ibb.co/6rctjZq/4386876d2cc0.jpg','https://i.ibb.co/w0rzHM9/49ac4752deaa.jpg','https://i.ibb.co/6Y405mp/78e301d02eea.jpg'

bios = '• من عرف الله هانت مصيبته، ومن أنس به زالت غربته ومن رضي بالقضاء سعد 🌼','الاستغفار يفتح الأقفال ويشرح البال ويكثر المال ويصلح الحال. 🙏','• في المآزق ينكشف لؤم الطباع، وفي الفتن تنكشف أصالة الرأي وفي الشدة ينكشف صدق الإخاء 💏','• فتح الله للمطالب أبواباً وسن للحوادث أسباباً فقال لنا : ادعوا، وقال : اعملوا 🙏','• هموم الدنيا مؤقتة، مهما طال زمنها لكنها في قلوبنا الضعيفة أكبر من الآخرة. 😔','• لا تندم على إحسان صادق بذلته فالطيور لا تأخذ مقابلاً على تغريدها.🫀','• اثنان لا تنساهما: ذكر الله والموت، واثنان لا تذكرهما: إحسانك للناس، وإساءتهم إليك.🌜','• الله يكتب لك بكل خطوة سعادة، وكل نظرة عبادة، وكل بسمة شهادة، وكل رزق زيادة. 🌱💛','• ضاعةُ الوقت أشد من الموتِ؛ لأنّ إضاعةُ الوقت تقطعك عن الله، والدار الآخرة، والموت يقطعك عن الدنيا وأهلها. 👌','• أطع الإله كما أُمر، واملأ فؤادك بالحذر، وأطع أباك فإنّه ربّاك من عهد الصّغر. ☘'

suu = 'اللّهم أصلح لي ديني الذي هو عصمة أمري، وأصلح لي دنياي التي فيها معاشي، وأصلح لي آخرتي التي فيها معادي، واجعل الحياة زيادة لي في كل خير، واجعل الموت راحةً لي من كل شر','يا مُقلّب القلوب ثبّت قلبي على دينك','اللّهم رب السّماوات ورب الأرض ورب العرش العظيم، ربنا ورب كل شيء، فالق الحب والنوى، ومنزل التوراة والإنجيل والفرقان، أعوذ بك من شر كل شيء أنت آخذ بناصيته، اللّهم أنت الأول فليس قبلك شيء، وأنت الآخر فليس بعدك شيء، وأنت الظاهر فليس فوقك شيء، وأنت الباطن فليس دونك شيء، اقضِ عنا الدين، وأغننا من الفقر.','اللّهم مالك الملك، تؤتي الملك من تشاء، وتنزع الملك ممن تشاء، وتعز من تشاء، وتذل من تشاء، بيدك الخير إنّك على كل شيء قدير، رحمن الدنيا والآخرة ورحيمهما، تعطيهما من تشاء، وتمنع منهما من تشاء، ارحمني رحمةً تغنيني بها عن رحمة من سواك.','اللّهم إني أسألك من الخير كله عاجله وآجله ما علمت منه وما لم أعلم، وأعوذ بك من الشر كله عاجله وآجله ما علمت منه وما لم أعلم، اللّهم إني أسألك من خير ما سألك منه عبدك ونبيك، وأعوذ بك من شر ما عاذ به عبدك ونبيك، اللّهم إني أسألك الجنة وما قرّب إليها من قولٍ أو عمل، وأسألك أن تجعل كل قضاءٍ قضيته لي خيرًا.','اللّهم اقسم لنا من خشيتك ما يحول بيننا وبين معاصيك، ومن طاعتك ما تبلغنا به جنتك، ومن اليقين ما يهون علينا مصيبات الدنيا، ومتعنا بأسماعنا وأبصارنا وقوتنا ما أحييتنا واجعله الوارث منا واجعل ثأرنا على من ظلمنا، وانصرنا على من عادانا، ولا تجعل مصيبتنا في ديننا، ولا تجعل الدنيا أكبر همنا ولا مبلغ علمنا، ولا تسلّط علينا من لا يرحمنا.','اللّهم عالم الغيب والشهادة، فاطر السماوات والأرض، رب كل شيء ومليكه، أشهد أنّ لا إله إلا أنت، أعوذ بك من شر نفسي وشر الشيطان وشركه.','اللّهم إنّي أعوذ بك من فتنة النار وعذاب النّار، وفتنة القبر وعذاب القبر، ومن شر فتنة الغنى ومن شر فتنة الفقر، وأعوذ بك من شر فتنة المسيح الدجال، اللّهم اغسل خطاياي بماء الثلج والبرد، ونقِّ قلبي من الخطايا كما نقيت الثوب الأبيض من الدنس، وباعد بيني وبين خطاياي كما باعدت بين المشرق والمغرب، اللّهم فإني أعوذ بك من الكسل والهرم والمأثم والمعزم.','اللّهم رحمتك أرجو فلا تكلني إلى نفسي طَرْفة عين وأصلح لي شأني كله لا إله إلا أنت','اللّهم إني عبدُك وابن عبدِك وابن أمتِك، ناصيتي بيدك، ماضٍ فيّ حكمُك، عدلٌ فيّ قضاؤك، أسألك بكل اسمٍ هو لك سمّيت به نفسك أو أنزلته في كتابك أو علّمت به أحد من خلقك أو استأثرت به في علم الغيب عندك أن تجعل القرآن ربيع قلبي ونور صدري وجلاء حزني وذهاب همّي.','يا حي يا قيوم برحمتك أستغيث أصلح لي شأني كله ولا تكلني إلى نفسي طَرْفة عيْن.','اللّهم إنّي أعوذ بك من الهمِّ والحَزَن والعجز والكسل والبخل والجبن وضلع الدَّيْن وغلبة الرجال'

k = types.InlineKeyboardMarkup()
k1 = types.InlineKeyboardButton(text='☘️ صور رمضانيه', callback_data='randphoto')
k2 = types.InlineKeyboardButton(text='🌙 ادعيه عشوائيه', callback_data='randdoa')
k3 = types.InlineKeyboardButton(text='🏵 أقتباسات دينيه', callback_data='randbios')
k4 = types.InlineKeyboardButton('🩵 صور ادعيه رمضانيه', callback_data='photoramdan')
k5 = types.InlineKeyboardButton('تلاوات', callback_data='quran')
k6 = types.InlineKeyboardButton('الشيخ نقشبندي', callback_data='nqsbndy')
kb = types.InlineKeyboardMarkup()
kb1 = types.InlineKeyboardButton(text='الرجوع', callback_data='backb')
kb2 = types.InlineKeyboardButton(text='تغيير الصوره', callback_data='anyphoto')
kb3 =types.InlineKeyboardButton(text='تغيير الصوره', callback_data='anyphotoramadan')
kb4 = types.InlineKeyboardButton(text='تغيير الدعاء', callback_data='changedoa')
kb.add(kb1,kb2)
kbb = types.InlineKeyboardMarkup()
kbbb = types.InlineKeyboardMarkup()
kbbb.add(kb1,kb4)
kbb.add(kb1,kb3)
k.add(k1,k2)
k.add(k3)
k.add(k4)
k.add(k5,k6)
kbs = types.InlineKeyboardMarkup()
kbs1 = types.InlineKeyboardButton(text='تغيير الاقتباس', callback_data='changebios')
kbs.add(kb1,kbs1)
mssg = """اهــلا بـك فـي بوت رمضان 😌💚🏮

اختر احد الخيارات الموجوده في الاسفل ❤️☘ """
linkos = 'https://i.ibb.co/sJNNGFJ/4fa3bb6f84b2.jpg','https://i.ibb.co/8NTK9bV/d30a1d7d6f69.jpg','https://i.ibb.co/FzhHbq7/1dc2c31e902d.jpg','https://i.ibb.co/Jptmqz0/b3e20e7b40a2.jpg','https://i.ibb.co/bXTjCM2/fe383713cf77.jpg','https://i.ibb.co/hY9Kmtf/9b99fa20f016.jpg','https://i.ibb.co/txpf8vr/848f133f3615.jpg','https://i.ibb.co/G2DQhcs/eead1d82ac66.jpg','https://i.ibb.co/LYZ6x7r/cbb062b0cd57.jpg','https://i.ibb.co/ctr1tqp/0582498ec00a.jpg','https://i.ibb.co/zPBbN4T/f9b418d46b52.jpg','https://i.ibb.co/R9mVCF7/34214a9aba03.jpg'
	
@bot.callback_query_handler(func=lambda call: True)
def tylaoa(call):
    if call.data == "quran":
        voices = "https://t.me/ALMORTAGELRSK/" + str(random.randint(7, 276))
        bot.send_voice(call.message.chat.id, voices, caption="""
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
    
tok = Config.TG_BOT_TOKEN
bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def sttart(message):
	bot.reply_to(message,mssg,reply_markup=k)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
	if call.message:
		if call.data == 'randphoto':
			image_url = random.choice(linkos)
			bot.send_photo(call.message.chat.id, image_url,reply_markup=kb)
		elif call.data == 'randdoa':
			ggm = random.choice(suu)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=ggm,reply_markup=kbbb)
		elif call.data == 'randbios':
			bio = random.choice(bios)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=bio,reply_markup=kbs)
		elif call.data == 'photoramdan':
			image_url1 = random.choice(linksramdan)
			bot.send_photo(call.message.chat.id, image_url1,reply_markup=kbb)
		elif call.data == 'backb':
			bot.send_message(call.message.chat.id,mssg,reply_markup=k)
		elif call.data == 'anyphoto':
			image_url = random.choice(linkos)
			bot.send_photo(call.message.chat.id, image_url,reply_markup=kb)
		elif call.data == 'anyphotoramadan':
			image_url1 = random.choice(linksramdan)
			bot.send_photo(call.message.chat.id, image_url1,reply_markup=kbb)
		elif call.data == 'changedoa':
			ggm = random.choice(suu)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=ggm,reply_markup=kbbb)
		elif call.data == 'quran':
			ggm = random.choice(suu)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=ggm,reply_markup=kbbbb)
		elif call.data == 'nqsbndy':
			ggm = random.choice(suu)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=ggm,reply_markup=kbbbb)	
		elif call.data == 'changebios':
			bio = random.choice(bios)
			bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=bio,reply_markup=kbs)
            
bot.polling()
"""
Dev /- @Almortagel_12
Ch /- @AlmortagelTech
In /- 2024/2/14
"""