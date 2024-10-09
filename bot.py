
from telebot.types import KeyboardButton,ReplyKeyboardMarkup, InlineKeyboardButton
from secret import *
from telebot import TeleBot, types

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def say_hello(message):
    btn1 = types.InlineKeyboardButton("start")
    btn2 = types.InlineKeyboardButton("website")
    btn3 = types.InlineKeyboardButton("address")
    btn4 = types.InlineKeyboardButton("social media")
    btn5 = types.InlineKeyboardButton("founders")
    btn6 = types.InlineKeyboardButton("courses")
    btn7 = types.InlineKeyboardButton("prices")
    btn8 = types.InlineKeyboardButton("developer")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.row(btn1,btn8)
    markup.row(btn2,btn3,btn4)
    markup.row(btn5, btn6, btn7)
    bot.send_message(message.chat.id, "Welcome to SoftClub", reply_markup=markup)

@bot.message_handler()
def handler(message):
    if message.text == "start":
        bot.send_message(message.chat.id, f"Salom aleykum {message.chat.username} khush omaded ba SoftClub info")
    elif message.text == "address":
        bot.send_message(message.chat.id, "Suroghai mo kuchai 'Rahimi 12', orientir pushti Prokuraturai generali {https://yandex.ru/profile/171328689610?no-distribution=1&view-state=mini&source=wizbiz_new_map_single}")
    elif message.text == "website":
        bot.send_message(message.chat.id, "sahifai rasmii mo: {https://www.softclub.tj}")
    elif message.text == "social media":
        bot.send_message(message.chat.id, "instagram: {https://www.instagram.com/explore/locations/111644748083180/softclubtj/recent/}")
    elif message.text == "courses":
        bot.send_message(message.chat.id, """ C++
        HTML
        Python
        C#
        JavaScript
        Flutter
        Design UX/UI
        more in our tg: {https://t.me/softclubtj} """)
    elif message.text == "founders":
        bot.send_message(message.chat.id, "Nurullo Sulaymonov")
    elif message.text == "prices":
        bot.send_message(message.chat.id, "Our courses` prices are from 800 to 1500")
    elif message.text == "developer":
        bot.send_message(message.chat.id, "Shamsiddin Arbobzoda 😊")
    else:
        bot.send_message(message.chat.id, "Khush omaded))")

bot.infinity_polling()





