# telegramBot1

# Взят со статьи из журнала Хакер
# https://xakep.ru/2021/11/28/python-telegram-bots/

# Эхо-бот

# echo_bot - эхо‑бот будет получать от пользователя текстовое сообщение и возвращать его.

import telebot
from config import token

# Создаем бота
bot = telebot.TeleBot(token)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    files = open("photo.png", 'rb')  # открываем картинку
    bot.send_photo(message.chat.id, photo=files, caption='фото')  # посылаем ее и текст к ней


# Запускаем бота
bot.polling(none_stop=True, interval=0)
