# telegramBot1

# Взят со статьи из журнала Хакер
# https://xakep.ru/2021/11/28/python-telegram-bots/

# Эхо-бот

# echo_bot - эхо‑бот будет получать от пользователя текстовое сообщение и возвращать его.

import telebot
# from config import token
token = "5969843689:AAFskKqCFHbh5pIHCkTQFPyStOVMRJl2G20"
# Загружаем список анекдотов из файла
# если текстовый файл находится не в каталоге программы, то пишем полный путь к нему
# "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)
f = open('fun.txt', 'r', encoding='UTF-8')
funs = f.read().split('\n')
f.close()

# Создаем бота
bot = telebot.TeleBot(token)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Проверка работы
    bot.send_message(message.chat.id, funs[0])
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
