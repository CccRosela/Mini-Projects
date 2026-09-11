# UNO Bank Card Game - www.101computing.net/uno-bank-card-game-using-python
import random, time
import re

print(" +------------------+")
print(" |                  |")
print(" |     UNO BANK     |")
print(" |    CARD GAME!    |")
print(" |                  |")
print(" +------------------+")
print("")
greenCards = ['+1', '+3', '+5', '+7']
blueCards = ['-2', '-4', '-6', '-8']
blackCards = ['x2', '/2', '+2!', '-2!']

deck = greenCards + blueCards + blackCards
print("Shuffling deck...")
random.shuffle(deck)
time.sleep(1)

draws = 10
balance = 10

while draws > 0:
    print("\nYour Current balance is: ", balance, "$")
    print("Drawing card...")
    time.sleep(1)
    card = deck.pop()
    print("Your card: " + card)

    number = re.search(r"([+-x/])(\d)([!]?)", card)
   
    if not number.group(3):
        if number.group(1) == "+":
            balance += int(number.group(2))
            draws -= 1
        elif number.group(1) == "-":
            balance -= int(number.group(2))
            draws -= 1
        elif number.group(1) == "x":
            balance *= int(number.group(2))
            draws -= 1
        elif number.group(1) == "/":
            balance /= int(number.group(2))
            draws -= 1
    if number.group(3):
        draws -= 1 
        if number.group(1) == "+":
            draws += int(number.group(2))
        else:
            draws -= int(number.group(2))

print("\nFinal balance: ", balance, "$")
