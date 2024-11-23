# Version 1.0.


# cmd:
## ffmpeg -version - before this install ffmpeg and add folder to path: C:\ffmpeg\bin
## pip install pyTelegramBotAPI - installing interface PyTelegramBot
## pip install comtypes
## pip install pycaw


# PyTeleBot_Sc20 

# adding all dirs for Bot
import telebot
from telebot import types
from telebot import apihelper
# adding all dirs for starting audio recordings
import os
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# proxy-server
apihelper.proxy = {'https': #address}
# initializing the bot
token = ''
bot = telebot.TeleBot(token)

# creates event handler for /start command
@bot.message_handler(commands=["start"])
def start(m, res=False):
    
    adm = [# Telegram IDs]
    if m.chat.id not in adm:
        bot.send_message(m.chat.id, 'Доступ заблокирован!')
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Выбрать сигнал")
        item2=types.KeyboardButton("Записать сообщение")
        info=types.KeyboardButton("Информация")
        markup.row(item1, item2)
        markup.row(info)
        bot.send_message(m.chat.id, 'Бот запущен:', reply_markup=markup)
        bot.send_message(m.chat.id, '📋Главное меню:', reply_markup=markup)
# creates messages handler from buttons values
@bot.message_handler(content_types=['text'])
def bot_message(m, res=False):
        # Information Button
        if m.text == 'Информация':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("Инструкция")
            item2=types.KeyboardButton("В главное меню")
            markup.row(item1)
            markup.row(item2)
            bot.send_message(m.chat.id, '🤖 PythonTelegramBot 🤖\n\nVersion: 1.0\nCreated by Kirichenko V.', reply_markup=markup)
        # Instruction Button
        elif m.text == "Инструкция":
            bot.send_message(m.chat.id, 'Бот включает в себя такие разделы, как:\n\n1. Выбрать сигнал - позволяет выбрать нужное оповещение из предложенных и вывести через громкоговорите по школе.\n\n2. Записать сообщение - позволяет самому ввести текст, которых будет воспроизведён громкоговорителями.\n\n3. Информация - Содержит в себе краткие сведения о боте и данную инструкцию.')
        # Record the message Button
        elif m.text == "Записать сообщение":
            bot.send_message(m.chat.id, '⛔ Раздел находится в разработке ⛔')
        # Select Signal Button
        elif m.text == 'Выбрать сигнал':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("1. Учебная тревога")
            item2=types.KeyboardButton("2. Минирование")
            item3=types.KeyboardButton("3. Закрыть двери")
            item4=types.KeyboardButton("4. Открыть двери")
            item5=types.KeyboardButton("5. Воздушная тревога")
            item6=types.KeyboardButton("6. УЧЕБНАЯ воздушная тревога")
            item7=types.KeyboardButton("7. Проверка системы")
            item8=types.KeyboardButton("8. ЛОЖНАЯ тревога")
            back=types.KeyboardButton("В главное меню")
            markup.row(item1,item2,item3)
            markup.row(item4,item5,item6)
            markup.row(item7,item8)
            markup.row(back)
            bot.send_message(m.chat.id, '🔊Сигналы:', reply_markup=markup)

        ## Alarm Signals: 
        # Button 1
        elif m.text == '1. Учебная тревога':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("ДА: 1. Учебная тревога")
            item2=types.KeyboardButton("Вернуться")
            item3=types.KeyboardButton("В главное меню")
            markup.row(item1,item2)
            markup.row(item3)
            bot.send_message(m.chat.id, '❗Подтвердите запуск:', reply_markup=markup)
        elif m.text == 'ДА: 1. Учебная тревога':
            bot.send_message(m.chat.id, "🎙Запущен сигнал 'Учебная тревога'🎙")
            volume.SetMasterVolumeLevel(0.0, None)
            os.startfile('1. TeachingAlarm.wav')
            time.sleep(60)
            volume.SetMasterVolumeLevel(-55.0, None)
        # Button 2
        elif m.text == '2. Минирование':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("ДА: 2. Минирование")
            item2=types.KeyboardButton("Вернуться")
            item3=types.KeyboardButton("В главное меню")
            markup.row(item1,item2)
            markup.row(item3)
            bot.send_message(m.chat.id, '❗Подтвердите запуск:', reply_markup=markup)
        elif m.text == 'ДА: 2. Минирование':
            bot.send_message(m.chat.id, "🎙Запущен сигнал 'Минирование'🎙")
            volume.SetMasterVolumeLevel(0.0, None)
            os.startfile('2. Bomb.wav')
            time.sleep(60)
            volume.SetMasterVolumeLevel(-55.0, None)
        # Button 3
        elif m.text == '3. Закрыть двери':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("ДА: 3. Закрыть двери")
            item2=types.KeyboardButton("Вернуться")
            item3=types.KeyboardButton("В главное меню")
            markup.row(item1,item2)
            markup.row(item3)
            bot.send_message(m.chat.id, '❗Подтвердите запуск:', reply_markup=markup)
        elif m.text == 'ДА: 3. Закрыть двери':
            bot.send_message(m.chat.id, "🎙Запущен сигнал 'Закрыть двери'🎙")
            volume.SetMasterVolumeLevel(0.0, None)
            os.startfile('3. CloseDoors.wav')
            time.sleep(60)
            volume.SetMasterVolumeLevel(-55.0, None)
        # Button 4
        elif m.text == '4. Открыть двери':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("ДА: 4. Открыть двери")
            item2=types.KeyboardButton("Вернуться")
            item3=types.KeyboardButton("В главное меню")
            markup.row(item1,item2)
            markup.row(item3)
            bot.send_message(m.chat.id, '❗Подтвердите запуск:', reply_markup=markup)
        elif m.text == 'ДА: 4. Открыть двери':
            bot.send_message(m.chat.id, "🎙Запущен сигнал 'Открыть двери'🎙")
            volume.SetMasterVolumeLevel(0.0, None)
            os.startfile("4. OpenDoors.wav")
            time.sleep(60)
            volume.SetMasterVolumeLevel(-55.0, None)
        # Button 5
        elif m.text == '5. Воздушная тревога':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("ДА: 5. Воздушная тревога")
            item2=types.KeyboardButton("Вернуться")
            item3=types.KeyboardButton("В главное меню")
            markup.row(item1,item2)
            markup.row(item3)
            bot.send_message(m.chat.id, '❗Подтвердите запуск:', reply_markup=markup)
        elif m.text == 'ДА: 5. Воздушная тревога':
            bot.send_message(m.chat.id, "🎙Запущен сигнал 'Воздушная тревога'🎙")
            volume.SetMasterVolumeLevel(0.0, None)
            os.startfile("5. AirAlarm.wav")
            time.sleep(60)
            volume.SetMasterVolumeLevel(-55.0, None)
        # Button 6
        elif m.text == '6. УЧЕБНАЯ воздушная тревога':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("ДА: 6. УЧЕБНАЯ воздушная тревога")
            item2=types.KeyboardButton("Вернуться")
            item3=types.KeyboardButton("В главное меню")
            markup.row(item1,item2)
            markup.row(item3)
            bot.send_message(m.chat.id, '❗Подтвердите запуск:', reply_markup=markup)
        elif m.text == 'ДА: 6. УЧЕБНАЯ воздушная тревога':
            bot.send_message(m.chat.id, "🎙Запущен сигнал 'УЧЕБНАЯ воздушная тревога'🎙")
            volume.SetMasterVolumeLevel(0.0, None)
            os.startfile("6. TeachingAirAlarm.wav")
            time.sleep(60)
            volume.SetMasterVolumeLevel(-55.0, None)
        # Button 7
        elif m.text == '7. Проверка системы':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("ДА: 7. Проверка системы")
            item2=types.KeyboardButton("Вернуться")
            item3=types.KeyboardButton("В главное меню")
            markup.row(item1,item2)
            markup.row(item3)
            bot.send_message(m.chat.id, '❗Подтвердите запуск:', reply_markup=markup)
        elif m.text == 'ДА: 7. Проверка системы':
            bot.send_message(m.chat.id, "🎙Запущен сигнал 'Проверка системы'🎙")
            volume.SetMasterVolumeLevel(0.0, None)
            os.startfile("7. SystemCheck.wav")
            time.sleep(60)
            volume.SetMasterVolumeLevel(-55.0, None)
        # Button 8
        elif m.text == '8. ЛОЖНАЯ тревога':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("ДА: 8. ЛОЖНАЯ тревога")
            item2=types.KeyboardButton("Вернуться")
            item3=types.KeyboardButton("В главное меню")
            markup.row(item1,item2)
            markup.row(item3)
            bot.send_message(m.chat.id, '❗Подтвердите запуск:', reply_markup=markup)
        elif m.text == 'ДА: 8. ЛОЖНАЯ тревога':
            bot.send_message(m.chat.id, "🎙Запущен сигнал 'ЛОЖНАЯ тревога'🎙")
            volume.SetMasterVolumeLevel(0.0, None)
            os.startfile("8. FalseAlarm.wav")
            time.sleep(60)
            volume.SetMasterVolumeLevel(-55.0, None)


        # Main Menu Button
        elif m.text == 'В главное меню':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("Выбрать сигнал")
            item2=types.KeyboardButton("Записать сообщение")
            settings=types.KeyboardButton("Информация")
            markup.row(item1, item2)
            markup.row(settings)
            bot.send_message(m.chat.id, '📋Главное меню:', reply_markup=markup)

        # Back Button
        elif m.text == 'Вернуться':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1=types.KeyboardButton("1. Учебная тревога")
            item2=types.KeyboardButton("2. Минирование")
            item3=types.KeyboardButton("3. Закрыть двери")
            item4=types.KeyboardButton("4. Открыть двери")
            item5=types.KeyboardButton("5. Воздушная тревога")
            item6=types.KeyboardButton("6. УЧЕБНАЯ воздушная тревога")
            item7=types.KeyboardButton("7. Проверка системы")
            item8=types.KeyboardButton("8. ЛОЖНАЯ тревога")
            back=types.KeyboardButton("В главное меню")
            markup.row(item1,item2,item3)
            markup.row(item4,item5,item6)
            markup.row(item7,item8)
            markup.row(back)
            bot.send_message(m.chat.id, '🔊Сигналы:', reply_markup=markup)

# check getting query
bot.infinity_polling(none_stop=True, interval=0)

