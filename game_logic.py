import random
from ascii_art import STAGES, MAX_MISTAKES

# List of secret words
# For testing
#WORDS = ["snowman"]
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, solution_list):
    print(STAGES[mistakes])
    print("Word: " + "".join(solution_list))

    
def play_game():
    secret_word = get_random_word()

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # create solution list with length of secret word
    # and fill it with underscores + padding
    solution_list = []
    for i in range(len(secret_word)):
        solution_list.append("_ ")

    mistakes = 0
    replaced_letters = 0

    while True:
        display_game_state(mistakes, solution_list)

        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or not len(guess) == 1:
            print("Please enter a single letter to save the snowman!")
            break

        print("You guessed:", guess)


        foundLetter = False
        # loop through the whole secret word to search for entered letter
        for char in secret_word:
            if char == guess: 
                foundLetter = True
                # add letter + padding to solution_list
                for i in range(len(secret_word)):
                    # if match and if letter was not replaced before
                    if secret_word[i] == guess and solution_list[i] == "_ ":
                        solution_list[i] = guess + " "
                        replaced_letters += 1

        if not foundLetter:
            mistakes += 1
        
        if mistakes == MAX_MISTAKES:
            print("Sorry, the snowman is gone!")
            break
        
        if replaced_letters == len(secret_word):
            print("Yay, you saved the snowman!") 
            break