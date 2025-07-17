from pyfiglet import Figlet
import sys
import random as r

figlet = Figlet()

def main():

    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        response = input("Input: ")
        new_font = figlet.setFont(font = r.choice(fonts))
        print(figlet.renderText(response))

    elif len(sys.argv) ==3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
            response = input("Input: ")
            newfont = figlet.setFont(font = sys.argv[2])
            print(figlet.renderText(response))
        else:
            sys.exit("Invalid prompt")

    else:
        sys.exit("Invalid prompt")

if __name__ ==  "__main__":
    main()


