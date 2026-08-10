from color import color

def addressVal(address,name):
    character = [".","@"]

    if any(char in address for char in character):
        print(f"Address: {color.BOLD}{color.UNDERLINE}{address}{color.END} is Valid!")
        print(f"Welcome, {color.DARKCYAN}{name}{color.END}")
    else:
        print(f"{color.RED} Invalid address! {color.END}")

name = input("What is your name?: ")
mail = input("What is your email address?: ")

addressVal(mail,name)
