# Text color addition
from color import color

def addressVal(address,name):
    character = [".","@"]

    if any(char in address for char in character) and (address.endswith("@gmail.com") or address.endswith("@yahoo.com")):
        print(f"Address: {color.BOLD}{color.UNDERLINE}{address}{color.END} is Valid!")
        print(f"Welcome, {color.DARKCYAN}{name}{color.END}")
    else:
        print(f"{color.RED} Invalid address! {color.END}")

name = input("What is your name?: ").title()
mail = input("What is your email address?: ")

addressVal(mail,name)
