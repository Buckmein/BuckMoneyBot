import requests
import json


values = {'Рубль': 'RUB',
          'Доллар': 'USD',
          'Евро': 'EUR'
          }  #Список доступных валют для добавления новой валюты необходимо просто дополнить этот словарь
r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
tree = json.loads(r.content)
tree = tree["Valute"]
TOKEN = "5895429023:AAHdY1Y1T7NBygJDI72ND9e4d8LQ9vw1deY"