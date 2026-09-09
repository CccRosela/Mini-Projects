morseCode = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


def encode_message(message):
    encoded_message = ""

    for char in message.upper():
        if char == " ":
            encoded_message += "/ "
            continue

        if char not in morseCode:
            raise ValueError(f"Character '{char}' cannot be converted to morse code.")

        encoded_message += morseCode[char] + " "

    return encoded_message.strip()


def main():
    message = input('Type a message to convert in morse code (e.g. "SOS"?): ').strip()

    if not message:
        print("No message provided.")
        return

    encoded_message = encode_message(message)
    print(f"Encoded message: {encoded_message}")


if __name__ == "__main__":
    main()

