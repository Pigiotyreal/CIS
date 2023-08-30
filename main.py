import random

print("Welcome to Crypto Investment Simulator! Type help to get help!")
print("You have $1000 to invest. Good luck!")

money = 1000
bitcoin = 0
eth = 0
doge = 0
ltc = 0

while True:
    command = input("> ")
    
    if command == "help":
        print("Commands:")
        print("help - Displays this message.")
        print("invest [crypto] [amount] - Invests the amount of money into the crypto.")
        print("sell [crypto] [amount] - Sells the amount of crypto.")
        print("wallet - Displays your wallet.")
        print("quit - Quits the simulation.")