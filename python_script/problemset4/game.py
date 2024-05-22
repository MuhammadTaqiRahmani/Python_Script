import random

def guess_game(ran_value,guess):
    if guess == ran_value:
        print("Just Right!!!")
    elif guess > ran_value:
        print("Too Large")
        x = input_guess()
        guess_game(ran_value,x)
    elif guess < ran_value:
        print("Too Small")
        x = input_guess()
        guess_game(ran_value,x)
    else:
        print("Please input Integer value.")


def input_level():
    control = True
    while control:
        try:
            level = int(input("Level: "))
            return level
        except ValueError:
            print("Invalid Input: Please input Integer value.")
    
def input_guess():
    control = True
    while control:
        try:
            guess = int(input("Guess: "))
            return guess
        except ValueError:
            print("Invalid Input: Please input Integer value.")
    


def main():
    LEVEL = input_level()
    GUESS = input_guess()
    ran_value = random.randint(1, LEVEL)
    
    guess_game(ran_value, GUESS)

    
if __name__=="__main__":
    main()