# Text color edit
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

text = input("Write a message here: ")

def text_edit(text):
    colors = {
        "{red}": color.RED,
        "{blue}": color.BLUE,
        "{cyan}": color.CYAN,
        "{green}": color.GREEN,
        "{purple}": color.PURPLE
    }

    for c, code in colors.items():
        text = text.replace(c, code)

    if ":)" in text:
        text = text.replace(":)", "🙂")
    if ":(" in text:
        text = text.replace(":(", "🙁")
    if "T_T" in text:
        text = text.replace("T_T", "😭")
    if ":D" in text:
        text = text.replace(":D", "😃")
    if ":p" in text:
        text = text.replace(":D", "😛")

    print(text)
    
text_edit(text)