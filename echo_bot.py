# echo_bot - эхо‑бот будет получать от пользователя текстовое сообщение и возвращать его.
import os

import telebot
import config
from config import token

# получение токена из файла настроек окружения .env в виде строки token = "1234567890"
# token = os.getenv("token")  # заменить токен при выгрузке в ГИТ на 'token'?

# Создаем бота
bot = telebot.TeleBot(token)


# Функция, обрабатывающая команду /start
#@bot.message_handler(commands=["start"])
#def start(m, res=False):
 #   bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


# Получение сообщений от юзера
#@bot.message_handler(content_types=["text"])
#def handle_text(message):
 #   bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


# Запускаем бота
#bot.polling(none_stop=True, interval=0)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
