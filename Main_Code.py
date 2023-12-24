import telebot
from datetime import datetime
import pytz


# start of online server proxy config
timezone = pytz.timezone("Asia/Kolkata") # Specify your timezone
weekday=datetime.now(timezone).weekday()
import urllib3
import telepot.api
proxy_url = 'http://proxy.server:3128'

telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30), }

telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1,
                                                             retries=False, timeout=30))

# end of online server proxy config


token = "5980084673:AAE2Sx4KEz3al3wHutO35Jsyq_SUN4UbTX8"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello!🤖\nI am JIIT bot.\n\nI am developed by @NukkadCodersbot\n\nTo get your time table:\nAfter sending /start \n1. Select your Batch. \n2. Select Day.\n\n\n\n• Kindly Report if you have any issues regarding bot as well as the Data bot returned \n', reply_markup=keyboardforbatches())
    bot.send_message(message.chat.id, ' Select you batch : \n', reply_markup=keyboardforbatches())

def keyboardforbatchesA1():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('CLASS AT PRESENT A1')
    btn2 = telebot.types.KeyboardButton('SELECT A DAY A1')
    btn3 = telebot.types.KeyboardButton('WHOLE WEEK A1')
    markup.add(btn1, btn2)
    return markup

def keyboardforbatchesA2():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('CLASS AT PRESENT A2')
    btn2 = telebot.types.KeyboardButton('SELECT A DAY A2')
    btn3 = telebot.types.KeyboardButton('WHOLE WEEK A2')
    markup.add(btn1, btn2)
    return markup
def keyboardforbatchesF6():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('CLASS AT PRESENT F7')
    btn2 = telebot.types.KeyboardButton('SELECT A DAY F7')
    btn3 = telebot.types.KeyboardButton('WHOLE WEEK F7')
    markup.add(btn1, btn2)
    return markup
def keyboardforbatchesF6():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('CLASS AT PRESENT F6')
    btn2 = telebot.types.KeyboardButton('SELECT A DAY F6')
    btn3 = telebot.types.KeyboardButton('WHOLE WEEK F4')
    markup.add(btn1, btn2)
    return markup
def keyboardforbatches():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('A1')
    btn2 = telebot.types.KeyboardButton('A2')
    btn3 = telebot.types.KeyboardButton('REPORT')
    btn4 = telebot.types.KeyboardButton('F6')
    #btn4 = telebot.types.KeyboardButton('F4')
    markup.add(btn1, btn2, btn4, btn3)
    return markup

@bot.message_handler(content_types=['text'])
def choice(message):
    #start of a1 ka weekday all
    current_time = datetime.now(timezone).time() # Extract the current time
    class_timeA1M = {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "9:00-11:50 Engineering Drawing & Design",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n2:00-2:50 L Electrical Science-I in G2",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "2:00-2:50 L Electrical Science-I in G2",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("15:50:00", "%H:%M:%S").time()): "3:00-3:50 T SDF-2 in S2",
        (datetime.strptime("15:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"
    }
    class_timeA1T= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 L Physics-2 in G8",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 T Physics-2 in TS-1",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 L SDF-2 in G3",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "No class right now\nNext Class is:\n1:00-1:50 T Electrical Science-1 in TS-2",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "1:00-1:50 T Electrical Science-1 in TS-2",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "2:00-2:50 L Mathematics-2 in G7",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("16:50:00", "%H:%M:%S").time()): "3:00-4:50 SDF-2 Lab in CL5",
        (datetime.strptime("16:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"
    }
    class_timeA1W= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 L English in G2",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 L Mathematics-2 in G2",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 L SDF-2 in G2",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "No class right now\nNext Class is:\n2:00-2:50 L Physics-2 in G2",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "2:00-2:50 L Physics-2 in G2",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("16:50:00", "%H:%M:%S").time()): "3:00-4:50 Physics-2 Lab in PL2",
        (datetime.strptime("16:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"
    }
    class_timeA1TH= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 L Mathematics-2 in G3",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 T Mathematics-2 in TS-2",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 L SDF-2 in G3",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "No class right now\nNext Class is:\n1:00-2:50 English Lab in LL",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "1:00-2:50 English Lab in LL",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"
    }
    class_timeA1F = {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 L Physics-2 in G2",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 L Electrical Science-1 in G8",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "No class right now\nNext Class is:\n1:00-2:50 Electrical Science Lab in BEL1",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "1:00-2:50 Electrical Science Lab in BEL1",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"
    }
    class_timeA1S= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "10:00-10:50 L Electrical Science-1 in G7",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"
    }
    #START OF A2 KA TT
    class_timeA2M = {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "10:00-11:50 Electrical Science Lab-I in BEL2",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n2:00-2:50 L Electrical Science-I in G2",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "2:00-2:50 L Electrical Science-I in G2",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("16:50:00", "%H:%M:%S").time()): "3:00-4:50  Engineering Drawing & Design",
        (datetime.strptime("16:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeA2T= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 L Physics-2 in G8",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 T Physics-2 in TS-2",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 L Software Development Fundamentals-II in G3",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n1:00-1:50 Electrical Science-I in TS-3",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "1:00-1:50 Electrical Science-I in TS-3",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "2:00-2:50 L Mathematics-2 in G7",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("16:50:00", "%H:%M:%S").time()): "3:00-4:50 P Software Development Fundamentals Lab-II in CL01",
        (datetime.strptime("16:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeA2W= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 L LIFE SKILLS AND EFFECTIVE COMMUNICATION in G2",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 L MATHEMATICS-II in G2",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 L Software Development Fundamentals-II in G2",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n1:00-1:50 T Engineering Drawing & Design in TS-3",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "1:00-1:50 T Engineering Drawing & Design in TS-3",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "2:00-2:50 L Physics-2 in G2",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("16:50:00", "%H:%M:%S").time()): "3:00-4:50 P Physics Lab-2 in PL1",
        (datetime.strptime("16:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeA2TH= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 L Mathematics-II in G3",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n11:00-11:50 L Software Development Fundamentals Lab-II in G3",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 L Software Development Fundamentals-II in G3",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n1:00-2:50 P LIFE SKILLS AND EFFECTIVE COMMUNICATION in CL12",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "1:00-2:50 P LIFE SKILLS AND EFFECTIVE COMMUNICATION in CL12",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("15:50:00", "%H:%M:%S").time()): "3:00-3:50 T Software Development Fundamentals -II in TS4",
        (datetime.strptime("15:50:00", "%H:%M:%S").time(), datetime.strptime("16:50:00", "%H:%M:%S").time()): "4:00-4:50 T Mathematics-II in TS1",
        (datetime.strptime("16:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeA2F = {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 L Physics-2 in G2",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 L Electrical Science-I in G8",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeA2S= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 L Electrical Science-I in G7",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    #START OF F4 KA TT
    class_timeF6M = {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "First Class on Monday is\n09:00-09:50 L Software Development Fundamentals-II in 228",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n11:00-12:50 P Software Development Fundamentals-II in 150",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "11:00-12:50 P Software Development Fundamentals-II in 150",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "1:00-1:50  L Electrical Science-I in 117",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "2:00-2:50  L Life Skills and Effective Communication in 117",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("16:50:00", "%H:%M:%S").time()): "3:00-4:50  P Life Skills and Effective Communication in HSS LAB",
        (datetime.strptime("16:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeF6T= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 T Software Development Fundamentals-II in 116",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n11:00-11:50 L Software Development Fundamentals-II in 228",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 L Software Development Fundamentals-II in 228",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n1:00-1:50 L Electrical Science-I in 117",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "1:00-1:50 L Electrical Science-I in 117",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "2:00-2:50 L Mathematics-2 in 117",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("15:50:00", "%H:%M:%S").time()): "3:00-3:50 L Physics-II in 117",
        (datetime.strptime("15:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeF6W= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 L MATHEMATICS-II in 117",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n11:00-11:50 T Mathematics-II in 116",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 T Mathematics-II in 116",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n1:00-3:50 P Engineering Workshop in WS-04",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("15:50:00", "%H:%M:%S").time()): "1:00-3:50 P Engineering Workshop in WS-04",
        (datetime.strptime("15:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeF6TH= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "12:00-1:50 P Physics Lab in 41",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("15:50:00", "%H:%M:%S").time()): "2:00-3:50 P Software Development Fundamentals Lab-II in 130",
        (datetime.strptime("15:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeF6F = {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("09:50:00", "%H:%M:%S").time()): "9:00-9:50 T Electrical Science-I in 116",
        (datetime.strptime("09:50:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 T Physics-II in 116",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 L Mathematics-II in 117",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("12:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n1:00-1:50 L Electrical Science-I in 117",
        (datetime.strptime("12:50:00", "%H:%M:%S").time(), datetime.strptime("13:50:00", "%H:%M:%S").time()): "1:00-1:50 L Electrical Science-I in 117",
        (datetime.strptime("13:50:00", "%H:%M:%S").time(), datetime.strptime("14:50:00", "%H:%M:%S").time()): "No Class right now\nNext Class is:\n3:00-3:50 L Physics-II in 226",
        (datetime.strptime("14:50:00", "%H:%M:%S").time(), datetime.strptime("15:50:00", "%H:%M:%S").time()): "3:00-3:50 L Physics-II in 226",
        (datetime.strptime("15:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    class_timeF6S= {
        (datetime.strptime("00:00:00", "%H:%M:%S").time(), datetime.strptime("10:50:00", "%H:%M:%S").time()): "10:00-10:50 L Software Development Fundamentals Lab-II in 228",
        (datetime.strptime("10:50:00", "%H:%M:%S").time(), datetime.strptime("11:50:00", "%H:%M:%S").time()): "11:00-11:50 L Physics-II in 228",
        (datetime.strptime("11:50:00", "%H:%M:%S").time(), datetime.strptime("23:59:59", "%H:%M:%S").time()): "No class now.\n Please select specific day"

    }
    #START OF F7 KA TT
    class_timeF7M = {
        (datetime.strptime("08:00:00", "%H:%M:%S").time(), datetime.strptime("09:00:00", "%H:%M:%S").time()): "MaA1th",
        (datetime.strptime("09:00:00", "%H:%M:%S").time(), datetime.strptime("10:00:00", "%H:%M:%S").time()): "Sc1AAience",
        (datetime.strptime("10:00:00", "%H:%M:%S").time(), datetime.strptime("11:00:00", "%H:%M:%S").time()): "EngAAlish",
        (datetime.strptime("11:00:00", "%H:%M:%S").time(), datetime.strptime("12:00:00", "%H:%M:%S").time()): "HisAAtory",
        (datetime.strptime("12:00:00", "%H:%M:%S").time(), datetime.strptime("13:00:00", "%H:%M:%S").time()): "LuncAAh Break",
        (datetime.strptime("13:00:00", "%H:%M:%S").time(), datetime.strptime("14:00:00", "%H:%M:%S").time()): "AAArt",
        (datetime.strptime("14:00:00", "%H:%M:%S").time(), datetime.strptime("15:00:00", "%H:%M:%S").time()): "ComAAputer Science",
        (datetime.strptime("17:00:00", "%H:%M:%S").time(), datetime.strptime("23:10:00", "%H:%M:%S").time()): "PhysdcicAAal Education"
    }
    class_timeF7T= {
        (datetime.strptime("08:00:00", "%H:%M:%S").time(), datetime.strptime("09:00:00", "%H:%M:%S").time()): "MaA1th",
        (datetime.strptime("09:00:00", "%H:%M:%S").time(), datetime.strptime("10:00:00", "%H:%M:%S").time()): "Sc1AAience",
        (datetime.strptime("10:00:00", "%H:%M:%S").time(), datetime.strptime("11:00:00", "%H:%M:%S").time()): "EngAAlish",
        (datetime.strptime("11:00:00", "%H:%M:%S").time(), datetime.strptime("12:00:00", "%H:%M:%S").time()): "HisAAtory",
        (datetime.strptime("12:00:00", "%H:%M:%S").time(), datetime.strptime("13:00:00", "%H:%M:%S").time()): "LuncAAh Break",
        (datetime.strptime("13:00:00", "%H:%M:%S").time(), datetime.strptime("14:00:00", "%H:%M:%S").time()): "AAArt",
        (datetime.strptime("14:00:00", "%H:%M:%S").time(), datetime.strptime("15:00:00", "%H:%M:%S").time()): "ComAAputer Science",
        (datetime.strptime("17:00:00", "%H:%M:%S").time(), datetime.strptime("23:10:00", "%H:%M:%S").time()): "PhysdcicAAal Education"
    }
    class_timeF7W= {
        (datetime.strptime("08:00:00", "%H:%M:%S").time(), datetime.strptime("09:00:00", "%H:%M:%S").time()): "MaA1th",
        (datetime.strptime("09:00:00", "%H:%M:%S").time(), datetime.strptime("10:00:00", "%H:%M:%S").time()): "Sc1AAience",
        (datetime.strptime("10:00:00", "%H:%M:%S").time(), datetime.strptime("11:00:00", "%H:%M:%S").time()): "EngAAlish",
        (datetime.strptime("11:00:00", "%H:%M:%S").time(), datetime.strptime("12:00:00", "%H:%M:%S").time()): "HisAAtory",
        (datetime.strptime("12:00:00", "%H:%M:%S").time(), datetime.strptime("13:00:00", "%H:%M:%S").time()): "LuncAAh Break",
        (datetime.strptime("13:00:00", "%H:%M:%S").time(), datetime.strptime("14:00:00", "%H:%M:%S").time()): "AAArt",
        (datetime.strptime("14:00:00", "%H:%M:%S").time(), datetime.strptime("15:00:00", "%H:%M:%S").time()): "ComAAputer Science",
        (datetime.strptime("17:00:00", "%H:%M:%S").time(), datetime.strptime("23:10:00", "%H:%M:%S").time()): "PhysdcicAAal Education"
    }
    class_timeF7TH= {
        (datetime.strptime("08:00:00", "%H:%M:%S").time(), datetime.strptime("09:00:00", "%H:%M:%S").time()): "MaA1th",
        (datetime.strptime("09:00:00", "%H:%M:%S").time(), datetime.strptime("10:00:00", "%H:%M:%S").time()): "Sc1AAience",
        (datetime.strptime("10:00:00", "%H:%M:%S").time(), datetime.strptime("11:00:00", "%H:%M:%S").time()): "EngAAlish",
        (datetime.strptime("11:00:00", "%H:%M:%S").time(), datetime.strptime("12:00:00", "%H:%M:%S").time()): "HisAAtory",
        (datetime.strptime("12:00:00", "%H:%M:%S").time(), datetime.strptime("13:00:00", "%H:%M:%S").time()): "LuncAAh Break",
        (datetime.strptime("13:00:00", "%H:%M:%S").time(), datetime.strptime("14:00:00", "%H:%M:%S").time()): "AAArt",
        (datetime.strptime("14:00:00", "%H:%M:%S").time(), datetime.strptime("15:00:00", "%H:%M:%S").time()): "ComAAputer Science",
        (datetime.strptime("17:00:00", "%H:%M:%S").time(), datetime.strptime("23:10:00", "%H:%M:%S").time()): "PhysdcicAAal Education"
    }
    class_timeF7F = {
        (datetime.strptime("08:00:00", "%H:%M:%S").time(), datetime.strptime("09:00:00", "%H:%M:%S").time()): "MaA1th",
        (datetime.strptime("09:00:00", "%H:%M:%S").time(), datetime.strptime("10:00:00", "%H:%M:%S").time()): "Sc1AAience",
        (datetime.strptime("10:00:00", "%H:%M:%S").time(), datetime.strptime("11:00:00", "%H:%M:%S").time()): "EngAAlish",
        (datetime.strptime("11:00:00", "%H:%M:%S").time(), datetime.strptime("12:00:00", "%H:%M:%S").time()): "HisAAtory",
        (datetime.strptime("12:00:00", "%H:%M:%S").time(), datetime.strptime("13:00:00", "%H:%M:%S").time()): "LuncAAh Break",
        (datetime.strptime("13:00:00", "%H:%M:%S").time(), datetime.strptime("14:00:00", "%H:%M:%S").time()): "AAArt",
        (datetime.strptime("14:00:00", "%H:%M:%S").time(), datetime.strptime("15:00:00", "%H:%M:%S").time()): "ComAAputer Science",
        (datetime.strptime("17:00:00", "%H:%M:%S").time(), datetime.strptime("23:10:00", "%H:%M:%S").time()): "PhysdcicAAal Education"
    }
    class_timeF7S= {
        (datetime.strptime("08:00:00", "%H:%M:%S").time(), datetime.strptime("09:00:00", "%H:%M:%S").time()): "MaA1th",
        (datetime.strptime("09:00:00", "%H:%M:%S").time(), datetime.strptime("10:00:00", "%H:%M:%S").time()): "Sc1AAience",
        (datetime.strptime("10:00:00", "%H:%M:%S").time(), datetime.strptime("11:00:00", "%H:%M:%S").time()): "EngAAlish",
        (datetime.strptime("11:00:00", "%H:%M:%S").time(), datetime.strptime("12:00:00", "%H:%M:%S").time()): "HisAAtory",
        (datetime.strptime("12:00:00", "%H:%M:%S").time(), datetime.strptime("13:00:00", "%H:%M:%S").time()): "LuncAAh Break",
        (datetime.strptime("13:00:00", "%H:%M:%S").time(), datetime.strptime("14:00:00", "%H:%M:%S").time()): "AAArt",
        (datetime.strptime("14:00:00", "%H:%M:%S").time(), datetime.strptime("15:00:00", "%H:%M:%S").time()): "ComAAputer Science",
        (datetime.strptime("17:00:00", "%H:%M:%S").time(), datetime.strptime("23:10:00", "%H:%M:%S").time()): "PhysdcicAAal Education"
    }

    if message.text == 'A1':
        bot.send_message(message.chat.id, 'Select day of the week : \n', reply_markup=keyboardforbatchesA1())
    elif message.text == 'A2':
        bot.send_message(message.chat.id, 'Select day of the week : \n', reply_markup=keyboardforbatchesA2())
    elif message.text == 'F6':
        bot.send_message(message.chat.id, 'Select day of the week : \n', reply_markup=keyboardforbatchesF6())
    elif message.text == 'F4':
        bot.send_message(message.chat.id, 'Select day of the week : \n', reply_markup=keyboardforbatchesF4())
    elif message.text == 'SELECT A DAY A1':
        bot.send_message(message.chat.id, 'Select day of the week : \n', reply_markup=keyboardforA1())
    elif message.text == 'SELECT A DAY A2':
        bot.send_message(message.chat.id, 'Select day of the week : \n', reply_markup=keyboardforA2())
    elif message.text == 'SELECT A DAY F6':
        bot.send_message(message.chat.id, 'Select day of the week : \n', reply_markup=keyboardforF6())
    elif message.text == 'SELECT A DAY F4':
        bot.send_message(message.chat.id, 'Select day of the week : \n', reply_markup=keyboardforF4())
    elif message.text == 'Monday A-1':
        bot.send_message(message.chat.id, 'Monday time table for Batch A1:\n9:00-11:50 Engineering Drawing & Design\n2:00-2:50 L Electrical Science-I in G2\n3:00-3:50 T SDF-2 in TS-2')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Tuesday A-1':
        bot.send_message(message.chat.id, 'Tuesday time table for Batch A1:\n9:00-9:50 L Physics-2 in G8\n10:00-10:50 T Physics-2 in TS-1\n11:00-11:50 L SDF-2 in G3\n1:00-1:50 T Electrical Science-1 in TS-2\n2:00-2:50 L Mathematics-2 in G7\n3:00-4:50 SDF-2 Lab in CL5')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Wed A-1':
        bot.send_message(message.chat.id, 'WED time table for Batch A1:\n9:00-9:50 L English in G2\n10:00-10:50 L Mathematics-2 in G2\n11:00-11:50 L SDF-2 in G2\n2:00-2:50 L Physics-2 in G2\n3:00-4:50 Physics-2 Lab in PL2')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Thursday A-1':
        bot.send_message(message.chat.id, 'Thur time table for Batch A1:\n9:00-9:50 L Mathematics-2 in G3\n10:00-10:50 T Mathematics-2 in TS-2\n11:00-11:50 L SDF-2 in G3\n1:00-2:50 English Lab in LL')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Friday A-1':
        bot.send_message(message.chat.id, 'Friday time table for Batch A1:\n9:00-9:50 L Physics-2 in G2\n10:00-10:50 L Electrical Science-1 in G8\n1:00-2:50 Electrical Science Lab in BEL1')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Saturday A-1':
        bot.send_message(message.chat.id, 'Sat time table for Batch A1:\n10:00-10:50 L Electrical Science-1 in G7')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Monday A-2':
        bot.send_message(message.chat.id, 'Monday time table for Batch A2:\n10:00-11:50 Electrical Science Lab-I in BEL2\n2:00-2:50 L Electrical Science-I in G2\n3:00-4:50  Engineering Drawing & Design')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Tuesday A-2':
        bot.send_message(message.chat.id, 'Tue  time table for Batch A2:\n9:00-9:50 L Physics-2 in G8\n10:00-10:50 T Physics-2 in TS-2\n11:00-11:50 L SDF-2 in G3\n1:00-1:50 Electrical Science-I in TS-3\n2:00-2:50 L Mathematics-2 in G7\n3:00-4:50 SDF-2 Lab in CL01')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Wed A-2':
        bot.send_message(message.chat.id, 'WED time table for Batch A2:\n9:00-9:50 L English in G2\n10:00-10:50 L MATHEMATICS-II in G2\n11:00-11:50 L SDF-2 in G2\n1:00-1:50 T Engineering Drawing & Design in TS-3\n2:00-2:50 L Physics-2 in G2\n3:00-4:50 P Physics Lab-2 in PL1')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Thursday A-2':
        bot.send_message(message.chat.id, 'Thur time table for Batch A2:\n9:00-9:50 L Mathematics-II in G3\n11:00-11:50 L SDF-2 in G3\n1:00-2:50 English Lab in CL12\n3:00-3:50 T SDF-2 in TS4\n4:00-4:50 T Mathematics-II in TS1')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Friday A-2':
        bot.send_message(message.chat.id, 'Fri time table for Batch A2:\n9:00-9:50 L Physics-2 in G2\n10:00-10:50 L Electrical Science-I in G8')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Saturday A-2':
        bot.send_message(message.chat.id, 'Sat time table for Batch A2:\n10:00-10:50 L Electrical Science-I in G7')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Monday F6':
        bot.send_message(message.chat.id, 'Monday time table for Batch F6 \n09:00-09:50 L Software Development Fundamentals-II in 228 \n11:00-12:50 P Software Development Fundamentals-II in 150 \n1:00-1:50  L Electrical Science-I in 117 \n2:00-2:50  L Life Skills and Effective Communication in 117 \n3:00-4:50  P Life Skills and Effective Communication in HSS LAB')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Tuesday F6':
        bot.send_message(message.chat.id, 'Tue  time table for Batch F6 \n9:00-9:50 T Software Development Fundamentals-II in 116\n11:00-11:50 L Software Development Fundamentals-II in 228\n1:00-1:50 L Electrical Science-I in 117\n2:00-2:50 L Mathematics-2 in 117 \n3:00-3:50 L Physics-II in 117')
        bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Wednesday F6':
        bot.send_message(message.chat.id, 'WED time table for Batch F6 \n9:00-9:50 L MATHEMATICS-II in 117\n11:00-11:50 T Mathematics-II in 116\n1:00-3:50 P Engineering Workshop in WS-04')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Thursday F6':
        bot.send_message(message.chat.id, 'Thur time table for Batch F6 \n12:00-1:50 P Physics Lab in 41\n2:00-3:50 P Software Development Fundamentals Lab-II in 130')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Friday F6':
        bot.send_message(message.chat.id, 'Fri time table for Batch F6 \n9:00-9:50 T Electrical Science-I in 116\n10:00-10:50 T Physics-II in 116\n11:00-11:50 L Mathematics-II in 117\n1:00-1:50 L Electrical Science-I in 117\n3:00-3:50 L Physics-II in 226')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Saturday F6':
        bot.send_message(message.chat.id, 'Sat time table for Batch F6 \n10:00-10:50 L Software Development Fundamentals Lab-II in 228\n11:00-11:50 L Physics-II in 228')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Monday F4':
        bot.send_message(message.chat.id, 'Monday time table for Batch F4')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Tuesday F4':
        bot.send_message(message.chat.id, 'Tue  time table for Batch F4')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Wednesday F4':
        bot.send_message(message.chat.id, 'WED time table for Batch F4')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Thursday F4':
        bot.send_message(message.chat.id, 'Thur time table for Batch F4')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Friday F4':
        bot.send_message(message.chat.id, 'Fri time table for Batch F4')
        bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'Saturday F4':
        bot.send_message(message.chat.id, 'Sat time table for Batch F4')
        bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'REPORT':
        bot.send_message(message.chat.id, 'If there is any discrepancy in the timetable, kindly email us at the address provided below. Also, if you would also like your batch to be featured in the bot, kindly email us at nukkadcoders@gmail.com')
        bot.send_message(message.chat.id, 'Select your batch : \n', reply_markup=keyboardforbatches())
    elif message.text == 'CLASS AT PRESENT A1':
        if weekday==0:
            for key, value in class_timeA1M.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==1:
            for key, value in class_timeA1T.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==2:
            for key, value in class_timeA1W.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==3:
            for key, value in class_timeA1TH.items():
                if current_time >= key[0] and current_time < key[1]:
                    text =value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==4:
            for key, value in class_timeA1F.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==5:
            for key, value in class_timeA1S.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==6:
            bot.send_message(message.chat.id,  "No class now (It's Sunday dude!!).\nPlease select specific day",reply_markup=keyboardforbatches())
    elif message.text == 'CLASS AT PRESENT A2':
        if weekday==0:
            for key, value in class_timeA2M.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==1:
            for key, value in class_timeA2T.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==2:
            for key, value in class_timeA2W.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==3:
            for key, value in class_timeA2TH.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==4:
            for key, value in class_timeA2F.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==5:
            for key, value in class_timeA2S.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==6:
            bot.send_message(message.chat.id,  "No class now (It's Sunday dude!!).\nPlease select specific day",reply_markup=keyboardforbatches())
    elif message.text == 'CLASS AT PRESENT F6':
        if weekday==0:
            for key, value in class_timeF6M.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==1:
            for key, value in class_timeF6T.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==2:
            for key, value in class_timeF6W.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==3:
            for key, value in class_timeF6TH.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==4:
            for key, value in class_timeF6F.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==5:
            for key, value in class_timeF6S.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
    elif message.text == 'CLASS AT PRESENT F7':
        if weekday==0:
            for key, value in class_timeF7M.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==1:
            for key, value in class_timeF7T.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==2:
            for key, value in class_timeF7W.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==3:
            for key, value in class_timeF7TH.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==4:
            for key, value in class_timeF7F.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())
        elif weekday==5:
            for key, value in class_timeF7S.items():
                if current_time >= key[0] and current_time < key[1]:
                    text = value
                    bot.send_message(message.chat.id, text)
                    bot.send_message(message.chat.id, 'Select you batch : \n', reply_markup=keyboardforbatches())
                    return
            bot.send_message(message.chat.id,  "No class now.\n Please select specific day",reply_markup=keyboardforbatches())

def keyboardforA1():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Monday A-1')
    btn2 = telebot.types.KeyboardButton('Tuesday A-1')
    btn3 = telebot.types.KeyboardButton('Wed A-1')
    btn4 = telebot.types.KeyboardButton('Thursday A-1')
    btn5 = telebot.types.KeyboardButton('Friday A-1')
    btn6 = telebot.types.KeyboardButton('Saturday A-1')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

def keyboardforA2():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Monday A-2')
    btn2 = telebot.types.KeyboardButton('Tuesday A-2')
    btn3 = telebot.types.KeyboardButton('Wed A-2')
    btn4 = telebot.types.KeyboardButton('Thursday A-2')
    btn5 = telebot.types.KeyboardButton('Friday A-2')
    btn6 = telebot.types.KeyboardButton('Saturday A-2')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

def keyboardforF6():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Monday F6')
    btn2 = telebot.types.KeyboardButton('Tuesday F6')
    btn3 = telebot.types.KeyboardButton('Wednesday F6')
    btn4 = telebot.types.KeyboardButton('Thursday F6')
    btn5 = telebot.types.KeyboardButton('Friday F6')
    btn6 = telebot.types.KeyboardButton('Saturday F6')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

def keyboardforF4():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Monday F4')
    btn2 = telebot.types.KeyboardButton('Tuesday F4')
    btn3 = telebot.types.KeyboardButton('Wednesday F4')
    btn4 = telebot.types.KeyboardButton('Thrusday F4')
    btn5 = telebot.types.KeyboardButton('Friday F4')
    btn6 = telebot.types.KeyboardButton('Saturday F4')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

print("parth is a og")

bot.polling()