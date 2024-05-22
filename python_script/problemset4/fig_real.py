import sys
import random
import pyfiglet

def main():
    if len(sys.argv) not in [1,3]:
        print("Invalid Command: Please Enter valid command.")
    elif len(sys.argv) == 1:
        font = random.choice(pyfiglet.FigletFont.getFonts())
        text = input("Enter the Text: ")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font = sys.argv[2]
            text = input("Enter the Text: ")
        else:
            print("-- Error --")
    
    figure = pyfiglet.Figlet(font)
    ren = figure.renderText(text)
    print(ren)

if __name__ == "__main__":
    main()
    
        