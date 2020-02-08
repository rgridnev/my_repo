import datetime

def dayscounter(year,mon,day, dest):
    now = datetime.datetime.today()
    NY = datetime.datetime(year,mon,day)
    d = NY-now #  str(d)  '83 days, 2:43:10.517807'
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    #result='1'
    #result=str(print(dest, 'через {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
    #result=print(dest, 'через {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
    mmm = (dest, 'через {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
    rrr=' '.join(mmm)
    return rrr

 
# Подключаем модуль для Телеграма

import telebot
from modules import tlgbotkey

# Указываем токен

bot = telebot.TeleBot(tlgbotkey)

 
# Импортируем типы из модуля, чтобы создавать кнопки

from telebot import types

# Настраиваем прокси
from telebot import apihelper
apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

 
# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    # Если написали «Привет»

    if message.text == "Привет":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет! Скажи куда ты собрался?")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_chegem = types.InlineKeyboardButton(text='Чегем', callback_data='chegem')

        # И добавляем кнопку на экран

        keyboard.add(key_chegem)

        key_splav = types.InlineKeyboardButton(text='Сплав с Олегом', callback_data='splav')

        keyboard.add(key_splav)
        
        key_veget = types.InlineKeyboardButton(text='Никуда', callback_data='veget')

        keyboard.add(key_veget)

        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Я скажу сколько ещё ждать', reply_markup=keyboard)


    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Привет")
        
 
# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    # Если нажали на одну из 12 кнопок — выводим гороскоп

    if call.data == "chegem": 

        # Формируем ответ

        msg = dayscounter(2020,4,25, 'Чегем')

        # Отправляем текст в Телеграм
        
    elif call.data == "splav":
        msg = dayscounter(2020,5,15, 'Сплав')
        
    elif call.data == "veget":
        msg = 'Овощ!'
        
    bot.send_message(call.message.chat.id, msg)

 
# Запускаем постоянный опрос бота в Телеграме

bot.polling(none_stop=True, interval=0)