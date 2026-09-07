morseCode = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E":  ".",
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

message = input("Type a message to convert in morse code (e.g. \"SOS\"?)").upper()
encodedMessage = ""

for char in message:
    if char in morseCode.keys():
        encodedMessage += morseCode[char] + " "
    else:
        raise ValueError(f"Character '{char}' cannot be converted to morse code.")

print(f"Encoded message: {encodedMessage}")

