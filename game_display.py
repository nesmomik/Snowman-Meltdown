from subprocess import call
import os
import sys
from game_assets import STAGES, MAX_MISTAKES


def clear_screen():
    call("clear" if os.name == "posix" else "cls")


def display_intro():
    clear_screen()

    print("Welcome to Snowman Meltdown!")

    print(STAGES[0])

    print(f"You can only make {MAX_MISTAKES} mistakes.")
    print("Can you save the snowman?")
    if input("Press enter key to continue, any key + enter to exit.\n"):
        sys.exit("Goodbye!")


def display_game_state(mistakes, solution_list):
    clear_screen()
    print(f"You only have {MAX_MISTAKES - mistakes} tries left.")
    print(STAGES[mistakes])
    print("Word: " + "".join(solution_list))

    
def display_input(mistakes, solution_list):
    validInput = False
    while not validInput:
        display_game_state(mistakes, solution_list)
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or not len(guess) == 1:
            print("Please enter a single letter to save the snowman!")
            if input("Press enter key to continue, any key + enter to exit.\n"):
                sys.exit("Goodbye!")
        else:
            validInput = True 

    print("You guessed:", guess)
     
    return guess


def display_win(mistakes, solution_list):
    display_game_state(mistakes, solution_list)
    print("Yay, you saved the snowman!") 
    if input("Press enter key to continue, any key + enter to exit.\n"):
        sys.exit("Goodbye!")


def display_loss(mistakes, solution_list):
    display_game_state(mistakes, solution_list)
    print("Sorry, the snowman is gone!") 
    if input("Press enter key to continue, any key + enter to exit.\n"):
        sys.exit("Goodbye!")