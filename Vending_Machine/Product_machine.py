from colorist import ColorHex

Products = {
    1: {
        "product": "Coca-Cola",
        "cost": 2.1
    },
    2: {
        "product": "Simple Sandwich",
        "cost": 5.6
    },
    3: {
        "product": "Special Sandwich",
        "cost": 7.9
    },
    4: {
        "product": "Fanta",
        "cost": 1.9
    },
    5: {
        "product": "Sprite",
        "cost": 1.9
    },
    6: {
        "product": "Chips",
        "cost": 2.1
    },
    7: {
        "product": "Spicy Chips",
        "cost": 2.2
    },
    8: {
        "product": "Water Bottle",
        "cost": 1.2
    },
    9: {
        "product": "Candy Bar",
        "cost": 3.9
    },
    10: {
        "product": "Cold Coffee",
        "cost": 4.3
    }
}

# Text color edit
def get_color(number):
    if number == 1:
        return ColorHex("#FAEBD7")
    elif number == 2:
        return ColorHex("#7FFFD4")
    elif number == 3:
        return ColorHex("#0000FF")
    elif number == 4:
        return ColorHex("#8A2BE2")
    elif number == 5:
        return ColorHex("#A52A2A")
    elif number == 6:
        return ColorHex("#5F9EA0")
    elif number == 7:
        return ColorHex("#FF7F50")
    elif number == 8:
        return ColorHex("#6495ED")
    elif number == 9:
        return ColorHex("#008B8B")
    elif number == 10:
        return ColorHex("#FF1493")
    else:
        return ColorHex.OFF