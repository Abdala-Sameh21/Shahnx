import telebot
from telebot import types

TOKEN = '7742479143:AAHzp86TrQwLngS7BPko2xcWRpmY3HW-cIo'
ADMIN_ID = 6662120440  # استبدل برقم ID الأدمن

bot = telebot.TeleBot(TOKEN)
orders = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("➕ إنشاء شحنة", "🚚 تتبع شحنة")
    if message.chat.id == ADMIN_ID:
        markup.add("🛠 لوحة تحكم الأدمن")
    bot.send_message(message.chat.id, "مرحباً بك في نظام شركة الشحن ShahenX!
اختر الخدمة المطلوبة:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    if message.text == "➕ إنشاء شحنة":
        bot.send_message(message.chat.id, "من فضلك أرسل تفاصيل الشحنة: الاسم + رقم الهاتف + العنوان.")
    elif message.text == "🚚 تتبع شحنة":
        bot.send_message(message.chat.id, "أرسل رقم الشحنة لتتبعها.")
    elif message.text == "🛠 لوحة تحكم الأدمن" and message.chat.id == ADMIN_ID:
        admin_panel(message)
    else:
        bot.send_message(message.chat.id, "رجاء اختر خيار من القائمة.")

def admin_panel(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📦 إضافة شحنة", "✏️ تحديث حالة شحنة", "❌ حذف شحنة", "📋 عرض كل الشحنات", "⬅️ رجوع")
    bot.send_message(message.chat.id, "لوحة تحكم الأدمن:", reply_markup=markup)

bot.polling()
