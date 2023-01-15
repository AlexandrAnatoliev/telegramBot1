# telegramBot1

[Ru] echo_bot - эхо‑бот будет получать от пользователя текстовое сообщение и возвращать его. 

Взят со статьи из журнала Хакер https://xakep.ru/2021/11/28/python-telegram-bots/

## Требования:
* $ pip install -r requirements.txt
* создать файл config.py, в котором будут храниться токен для доступа к боту в виде
```python 
token = "1234567890:ASDFGHH..."
```

## Где взять token?
* https://xakep.ru/2021/11/28/python-telegram-bots/

## Примеры использования

#### Функция, обрабатывающая команду /start
```python
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
```

#### Получение сообщений от юзера
```python
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    files = open("photo.png", 'rb')  # открываем картинку
    bot.send_photo(message.chat.id, photo=files, caption='фото')  # посылаем ее и текст к ней
```
#### Посылаем картинку пользователю
Размещаем файл с фото "photo.png" в рабочем каталоге. Добавляем текстовую часть к ней "caption='фото'"
```python
    files = open("photo.png", 'rb')  # открываем картинку
    bot.send_photo(message.chat.id, photo=files, caption='фото')  # посылаем ее и текст к ней
```
#### Запускаем бота
```python
bot.polling(none_stop=True, interval=0)
```