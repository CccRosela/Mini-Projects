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
    "Z": "--.."
}

morseCode["1"] = ".----"
morseCode["2"] = "..---"
morseCode["3"] = "...--"
morseCode["4"] = "....-"
morseCode["5"] = "....."
morseCode["6"] = "-...."
morseCode["7"] = "--..."
morseCode["8"] = "---.."
morseCode["9"] = "----."
morseCode["0"] = "-----"

message = input("Type a morse code message to decode: (e.g. \".... ..\" to \"HI\"): ").upper().strip()
encodedMessage = ""

for char in message.split(" "):
    for key, value in morseCode.items():
        if char == value:
            encodedMessage += key
            break
    else:
        raise ValueError(f"Character '{char}' cannot be converted from morse code.")

print(f"Decoded message: {encodedMessage}")