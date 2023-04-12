# Uses pyfiglet to draw an input string, requires zero or two CLI arguments, requiring the first to be '-f' or '-font'
# Zero arguments randomizes the string, or second argument defines the font to be used. 

from pyfiglet import Figlet
import random
figlet = Figlet()
import sys
fontList = figlet.getFonts()
quote = ''

#Check for too many or too few arguments
if len(sys.argv) >= 4:
    print("Too many arguments, please try again!")
    quit()
elif len(sys.argv) == 2:
        print("Can't use only one argument, Sorry!")
        quit()
# Check that first argument is correct, then checks second against font list
elif len(sys.argv) == 3:
        if sys.argv[1] not in ('-f', '-font'):
                print("Incorrect first argument, please try again!")
                quit()
        elif sys.argv[2] not in fontList:
              print("Sorry, that isn't a valid font name!")
              quit()
        #Request string and print with defined text
        else:
            quote = input("Please enter a string!")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(quote))
#Request string and print with random font        
else:
    quote = input("Please enter a string!")
    figlet.setFont(font=random.choice(fontList))
    print(figlet.renderText(quote))
