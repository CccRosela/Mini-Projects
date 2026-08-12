from colorist import ColorHex
from pyfiglet import Figlet
import random


fonts = Figlet().getFonts()
rand = random.choice(fonts)
figlet = Figlet()

names = []

while True:
    user = input("Enter a name (or 'exit'): ")
    if user == "exit":
        break
    else:
        names.append(user.strip().title())


if len(names) == 2:
    figlet.setFont(font= rand)
    print (f"{ColorHex('#93C572')} {figlet.renderText('Goodbye to')} \n{names[0]} and {names[1]}! {ColorHex.OFF}👋")

else:
    empty = ""
    for index, name in enumerate(names, start= 1):
        if index == len(names) - 1:
            empty += name + ', and '  # second to last person
        elif index == len(names):
            empty += name # index of last person
        elif index != len(names):
            empty += name + ', ' # all other people

    figlet.setFont(font= rand)
    print (f"\n{ColorHex('#93C572')}{figlet.renderText('Goodbye to')} \n{empty}! {ColorHex.OFF}👋")