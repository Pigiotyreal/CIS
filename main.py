import requests
import time
import threading

print("Welcome to Crypto Investment Simulator! Type help to get help!")
print("You have $1000 to invest. Good luck!")

money = 1000
btc = 0
eth = 0
doge = 0
ltc = 0

btc_price = 0
eth_price = 0
doge_price = 0
ltc_price = 0

def getPrice():
    global btc_price, eth_price, doge_price, ltc_price
    btc_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()["bitcoin"]["usd"]
    eth_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd").json()["ethereum"]["usd"]
    doge_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd").json()["dogecoin"]["usd"]
    ltc_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd").json()["litecoin"]["usd"]

def updatePrices():
    while True:
        getPrice()
        time.sleep(20)

threading.Thread(target=updatePrices).start()

while True:
    command = input("> ")
    command = command.lower()
    
    if command == "help":
        print("Commands: help, buy, sell, wallet, price, quit")
    
    elif command == "price":
        print("Bitcoin (BTC) price: $", btc_price)
        print("Ethereum (ETH) price: $", eth_price)
        print("Dogecoin (DOGE) price: $", doge_price)
        print("Litecoin (LTC) price: $", ltc_price)