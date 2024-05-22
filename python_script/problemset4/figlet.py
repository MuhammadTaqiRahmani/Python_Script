import sys
import random
import pyfiglet

def print_usage():
    print("Usage: python figlet.py [-f FONT] [TEXT]")
    print("Options:")
    print("  -f, --font  Specify font to use for text output")
    sys.exit(1)

def main():
    if len(sys.argv) not in [1, 3]:
        print_usage()

    if len(sys.argv) == 1:
        font = random.choice(pyfiglet.FigletFont.getFonts())
        text = input("Enter text: ")
    elif len(sys.argv) == 3:
        if sys.argv[1] in ("-f", "--font"):
            font = sys.argv[2]
            if font not in pyfiglet.FigletFont.getFonts():
                sys.exit("Error: Invalid font name")
            text = input("Enter text: ")
        else:
            print_usage()

    fig = pyfiglet.Figlet(font=font)
    print(fig.renderText(text))

if __name__ == "__main__":
    main()
