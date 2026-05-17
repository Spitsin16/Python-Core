import requests
import time

url = "https://api.rapira.net/open/market/rates" # ссылка откуда берем данные

bitcoin_prices=[]

for i in range(1):
    responce = requests.get(url) # получаем данные
    data = responce.json()  # открываем для чтения
    rates = data['data']
    usdt_rub=rates[0]
    coin=usdt_rub['symbol']
    price=usdt_rub['close']
    bitcoin_prices.append(price)
    time.sleep(1)

print(bitcoin_prices)

