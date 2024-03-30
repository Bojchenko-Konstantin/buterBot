from random import choice, random
import telebot

TOKEN='7157043888:AAGQT2eWN13Ntu3HWvHjzNuGZxZW7nsoh9k'
bot=telebot.TeleBot(TOKEN)

def generate_random_card():
    CARD_NUMBER = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    CARD_SUIT = ['Черви', 'Бубны', 'Пики', 'Трефы']
    random_card_number=choice(CARD_NUMBER)
    random_card_suit=choice(CARD_SUIT)
    return random_card_number, random_card_suit


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Добро пожаловать в игру! 
Я загадаю случайную карту,
а твоя задача - угадать её.\n''')
    keyboard=telebot.types.ReplyKeyboardMarkup()
    red_button=telebot.types.KeyboardButton("🟥")
    black_button=telebot.types.KeyboardButton("⬛️")

    keyboard.row(red_button)
    keyboard.row(black_button)

    bot.send_message(message.chat.id, 'Какого цвета загаданная мной карта: 🟥 или ⬛️', reply_markup=keyboard)
    bot.register_next_step_handler(message, compare_message)

def compare_message(message):
    card_number, card_suit=generate_random_card()
    if message.text == "🟥" and card_suit in ['Черви', 'Бубны']:
        bot.send_message(message.chat.id,'Верно! Карта, которую я загадал '+ card_number + '-' + card_suit)
    elif message.text == "⬛️" and card_suit in ['Пики', 'Трефы']:
        bot.send_message(message.chat.id,'Верно! Карта, которую я загадал ' + card_number + '-' + card_suit)
    else:
        bot.send_message(message.chat.id, 'Не повезло! Эта карта была ' + card_number + '-' + card_suit)



bot.infinity_polling()






