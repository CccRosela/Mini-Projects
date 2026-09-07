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

message = input("Type a message to convert in morse code (e.g. \"SOS\"?): ").upper()
encodedMessage = ""

for char in message:
    if char in morseCode.keys():
        encodedMessage += morseCode[char] + " "
    else:
        raise ValueError(f"Character '{char}' cannot be converted to morse code.")

print(f"Encoded message: {encodedMessage}")

