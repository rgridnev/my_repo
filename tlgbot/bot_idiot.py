from modules import dayscounter
 
# Подключаем модуль для Телеграма

import telebot
from modules import tlgbotkey, dialogflowtoken

# Указываем токен

bot = telebot.TeleBot(tlgbotkey)

#импортруем библиотеки для работы с JSON и flowtoken
import apiai, json

 
# Импортируем типы из модуля, чтобы создавать кнопки

from telebot import types

# Настраиваем прокси
from telebot import apihelper
apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    #bot.forward_message(127924504, message.chat_id, message_id)
    GODmsg="Сообщение " + message.text + " от " + str(message.from_user)
    bot.send_message(127924504, GODmsg)
    if message.text == "Сколько ещё ждать?" or message.text == "/wait":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Скажи, куда ты собрался?")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_chegem = types.InlineKeyboardButton(text='Чегем', callback_data='chegem')

        # И добавляем кнопку на экран

        keyboard.add(key_chegem)

        key_splav = types.InlineKeyboardButton(text='Сплав с Олегом', callback_data='splav')

        keyboard.add(key_splav)
      
        key_chuhloma = types.InlineKeyboardButton(text='Чухлома', callback_data='chuhloma')

        keyboard.add(key_chuhloma)

        key_bear = types.InlineKeyboardButton(text='Камчатка', callback_data='bear')  

        keyboard.add(key_bear)

        key_veget = types.InlineKeyboardButton(text='Никуда', callback_data='veget')

        keyboard.add(key_veget)

        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Я скажу сколько ещё ждать', reply_markup=keyboard)
    elif message.text == '/ID':
        IDmsg="Ваш ID в Телеграм: "+str(message.from_user.id)
        bot.send_message(message.from_user.id, IDmsg)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Сколько ещё ждать? или /wait - расчёт дней до ближайшей поездки. /ID - покажет ваш ID в Telegram. На любой другой запрос ответит встроенный искуственный идиот")
    elif message.text == '/start':
        bot.send_message(message.from_user.id, "Привет! Я умею рассказывать сколько дней до ближайшей поездки (для этого надо спросить 'Сколько ещё ждать?') или можем просто поболтать о жизни с помощью моего искуственного интеллекта.")
    else:
        request = apiai.ApiAI(dialogflowtoken).text_request() # Токен API к Dialogflow
        request.lang = 'ru' # На каком языке будет послан запрос
        request.session_id = 'Bot_Idiot' # ID Сессии диалога (нужно, чтобы потом учить бота)
        request.query = message.text # Посылаем запрос к ИИ с сообщением от юзера
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
        # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
        if response:
            bot.send_message(message.from_user.id, response)
        else:
            bot.send_message(message.from_user.id, 'Я Вас не совсем понял! Попробуйте повторить запрос или введите команду /help для получения справки')
        #msg=message.text+' Я всё понял, пользователь с ID '+str(message.from_user.id)
        #bot.send_message(message.from_user.id, msg)

# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    # Если нажали на одну из 12 кнопок — выводим гороскоп

    if call.data == "chegem": 

        # Формируем ответ

        msg = dayscounter(2020,4,25, 'На Кавказ, ближе к небу')

        # Отправляем текст в Телеграм
        
    elif call.data == "bear":
        msg = dayscounter(2020,8,7, 'На корм медведям')

    elif call.data == "splav":
        msg = dayscounter(2020,5,15, 'На корм акулам Оки')

    elif call.data == "chuhloma":
        msg = dayscounter(2020,6,11, 'В Костромские леса')
        
    elif call.data == "veget":
        msg = 'Овощ!'
        
    bot.send_message(call.message.chat.id, msg)

# Запускаем постоянный опрос бота в Телеграме

bot.polling(none_stop=True, interval=0)

