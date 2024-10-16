from pyfiglet import Figlet
from sys import argv, exit
from random import choice
figlet = Figlet()

if len(argv) == 1:

    figlet.setFont(font=choice(figlet.getFonts()))
    
elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
    try:
        figlet.setFont(font=argv[2])
    except:
        print("Invalid usage")
        exit(1)

else:
    print("Invalid usage")
    exit(1)


msg = input("Input: ")
print(figlet.renderText(msg))

'''
FEW FONTS
* Standard
* Small
* Big
* Slant
* 3-D
* Gothic
* Cursive
* Bubble
* Rectangle
* Alphabet
'''