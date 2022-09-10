"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from itertools import tee
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


""" PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
} """


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def name_planet(update, context):
    user_text = update.message.text
    comm_planet = user_text.split()
    

    print(user_text)
    update.message.reply_text(user_text)


def planet_search(update, context):

    name = ephem.update.message.text('2000/01/01') #определение планеты в настоящее время
    constellation = ephem.constellation(update.message.text) #скажет в каком созвездии была планета на определенную дату
    print(constellation)

def main():
    mybot = Updater("5494600204:AAGsihHglAuzcThN_CxTVL-aQo2CLJxQG0A", use_context=True) #request_kwargs=PROXY,

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, name_planet))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
