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
    elif command == "quit":
        print("Thanks for playing!")
        break
    elif command == "wallet":
        print(f"Money: ${money:.2f}")
        print(f"Invested: ${btc*btc_price + eth*eth_price + doge*doge_price + ltc*ltc_price:.2f}")
        print(f"Bitcoin: {btc} BTC (${btc*btc_price:.2f})")
        print(f"Ethereum: {eth} ETH (${eth*eth_price:.2f})")
        print(f"Dogecoin: {doge} DOGE (${doge*doge_price:.2f})")
        print(f"Litecoin: {ltc} LTC (${ltc*ltc_price:.2f})")
    elif command.startswith("buy"):
        command = command.split()
        if len(command) == 3:
            coin = command[1]
            amount = command[2]
            if coin == "btc":
                if money >= btc_price * float(amount):
                    money -= btc_price * float(amount)
                    btc += float(amount)
                    print(f"You bought {amount} BTC!")
                else:
                    print("You don't have enough money!")
            elif coin == "eth":
                if money >= eth_price * float(amount):
                    money -= eth_price * float(amount)
                    eth += float(amount)
                    print(f"You bought {amount} ETH!")
                else:
                    print("You don't have enough money!")
            elif coin == "doge":
                if money >= doge_price * float(amount):
                    money -= doge_price * float(amount)
                    doge += float(amount)
                    print(f"You bought {amount} DOGE!")
                else:
                    print("You don't have enough money!")
            elif coin == "ltc":
                if money >= ltc_price * float(amount):
                    money -= ltc_price * float(amount)
                    ltc += float(amount)
                    print(f"You bought {amount} LTC!")
                else:
                    print("You don't have enough money!")
            else:
                print("Invalid coin!")
        else:
            print("Invalid command!")
    elif command.startswith("sell"):
        command = command.split()
        if len(command) == 3:
            coin = command[1]
            amount = command[2]
            if coin == "btc":
                if btc >= float(amount):
                    money += btc_price * float(amount)
                    btc -= float(amount)
                    print(f"You sold {amount} BTC!")
                else:
                    print("You don't have enough BTC!")
            elif coin == "eth":
                if eth >= float(amount):
                    money += eth_price * float(amount)
                    eth -= float(amount)
                    print(f"You sold {amount} ETH!")
                else:
                    print("You don't have enough ETH!")
            elif coin == "doge":
                if doge >= float(amount):
                    money += doge_price * float(amount)
                    doge -= float(amount)
                    print(f"You sold {amount} DOGE!")
                else:
                    print("You don't have enough DOGE!")
            elif coin == "ltc":
                if ltc >= float(amount):
                    money += ltc_price * float(amount)
                    ltc -= float(amount)
                    print(f"You sold {amount} LTC!")
                else:
                    print("You don't have enough LTC!")
            else:
                print("Invalid coin!")
        else:
            print("Invalid command!")