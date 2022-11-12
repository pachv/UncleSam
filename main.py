from distutils.command.config import config
from bs4 import BeautifulSoup
import requests
import random
#новый функционал
#Пошутить
#Предложить рецепт
#Записать в календарь
#Учет расходов
import telebot
from telebot import types

import api_key
API_K = api_key.token

# pip install beautifulsoup4 lxml requests telebot


#! Receipts Functions

def getReceipt(url, tag, clas):
    request = requests.get(url)

    receipts = BeautifulSoup(request.text, "lxml").find_all(tag, class_=clas)
    return receipts


receipts = getReceipt("https://vc.ru/", "title", "")
receipts = [i.text for i in receipts]


#! Bot Configurstion

bot = telebot.TeleBot(API_K)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("привет")

    markup.add(item1)

    bot.send_message(
        message.chat.id, "Выберите сайт, от которого хотете получить рецепт", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def botMessage(message):
    if message.text == "привет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        getReceipt = types.KeyboardButton('получить рецепт')
        back = types.KeyboardButton("Назад")

        markup.add(back, getReceipt)

        bot.send_message(message.chat.id, "Привет", reply_markup=markup)


bot.polling()
