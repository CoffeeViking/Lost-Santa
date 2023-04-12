from pyfiglet import Figlet
import random
import sys
figlet = Figlet()
fontList = figlet.getFonts()

if len(sys.argv) == 2 or len(sys.argv) >= 4:
        print("Error: Error Code 123 easy as abc ")
        quit()
else:
        quote = input("Please Enter a string of text!")
if len(sys.argv) == 3:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(quote))
else:
        figlet.setFont(font=random.choice(fontList))
        print(figlet.renderText(quote))
