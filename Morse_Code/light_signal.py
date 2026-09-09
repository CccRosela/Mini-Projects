from encoder import morseCode

import time
import turtle


def flash_light(light, duration):
    light.showturtle()
    screen.update()
    time.sleep(duration)
    light.hideturtle()
    screen.update()
    time.sleep(0.2)


screen = turtle.Screen()
screen.title("Morse Code Light Signal")
screen.screensize(200, 200)
screen.bgcolor("black")
screen.tracer(0)

light = turtle.Turtle()
light.shape("circle")
light.color("yellow")
light.shapesize(7, 7)
light.hideturtle()


def transmit_message(message):
    message = message.upper().strip()

    if not message:
        return

    for index, char in enumerate(message):
        if char == " ":
            time.sleep(0.7)
            continue

        morse_symbol = morseCode.get(char)
        if morse_symbol is None:
            raise ValueError(f"Character '{char}' cannot be converted to morse code.")

        for symbol in morse_symbol:
            if symbol == "-":
                duration = 0.6
            else:
                duration = 0.2
                
            flash_light(light, duration)


if __name__ == "__main__":
    user_message = input('Type a message to flash in Morse code: ').strip()
    transmit_message(user_message)
