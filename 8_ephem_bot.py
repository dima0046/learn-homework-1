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
from datetime import date

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
    update.message.reply_text('Use command "/planet [name]"')


def name_planet(update, context):
    
    #Принимаем значение от пользователя
    user_text = update.message.text.split()
    #Сегодняшняя дата
    today = date.today().strftime("%Y/%m/%d")
    planet_name = user_text[1].capitalize()
    #Поиск планеты
    if user_text[0] == '/planet' and len(user_text) < 2:
      #Определение планет на сегодня
      if planet_name == 'Mars':
        constellation = ephem.constellation(ephem.Mars(today))
      elif planet_name == 'Jupiter':
        constellation = ephem.constellation(ephem.Jupiter(today))
      elif planet_name == 'Saturn':
        constellation = ephem.constellation(ephem.Saturn(today))
      else:
          update.message.reply_text('Unknown planet. Please try again')
      update.message.reply_text(f'Planete {planet_name} is in {constellation[1]}')
    else:
      update.message.reply_text('Unknown command. Please try again')
      return

def main():
    mybot = Updater("5494600204:AAGsihHglAuzcThN_CxTVL-aQo2CLJxQG0A", use_context=True) #request_kwargs=PROXY,
    
    dp = mybot.dispatcher

    dp.start
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, name_planet))  

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
