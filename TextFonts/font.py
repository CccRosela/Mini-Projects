import sys
import random
from pyfiglet import Figlet
from colorist import ColorHex 

figlet = Figlet()
fonts = Figlet().getFonts()

if len(sys.argv) not in [1, 3]:
    sys.exit(f"{ColorHex('#800000')}Invalid.")
elif len(sys.argv) == 3:
    if sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts:
        figlet.setFont(font= sys.argv[2])
        user = input("Text to style: ")
        print(figlet.renderText(user))
    else:
        sys.exit(f"{ColorHex('#800000')}Invalid.")
elif len(sys.argv) == 1:
    rand = random.choice(fonts)
    figlet.setFont(font = rand)
    user = input("Text to style: ")
    print(figlet.renderText(user))