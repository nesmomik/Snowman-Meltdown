import random


# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

MAX_MISTAKES = 4

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, solution_list):
    print(STAGES[mistakes])
    print("Word: " + str(solution_list))
     

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
    while True:
        display_game_state(mistakes, solution_list)

        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        # TODO Game logic:
        # loop through the whole secret word to search for entered letter
        # if letter found fill letter into solution list
        # if not increase mistakes counter

        # TESTING:
        mistakes += 1

        if mistakes == MAX_MISTAKES:
            break



if __name__ == "__main__":
    play_game()