import random
import requests
import time
import asyncio

print("Welcome to Crypto Investment Simulator! Type help to get help!")
print("You have $1000 to invest. Good luck!")

money = 1000
btc = 0
eth = 0
doge = 0
ltc = 0

async def getPrice():
    btc_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()["bitcoin"]["usd"]
    eth_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd").json()["ethereum"]["usd"]
    doge_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd").json()["dogecoin"]["usd"]
    ltc_price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd").json()["litecoin"]["usd"]
    return btc_price, eth_price, doge_price, ltc_price

async def main():
    while True:
        btc_price, eth_price, doge_price, ltc_price = await getPrice()
        print(f"BTC Price: {btc_price}")
        print(f"ETH Price: {eth_price}")
        print(f"DOGE Price: {doge_price}")
        print(f"LTC Price: {ltc_price}")
        await asyncio.sleep(20)

asyncio.run(main())