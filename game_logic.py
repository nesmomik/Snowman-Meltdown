import random

from game_assets import MAX_MISTAKES, WORDS
from game_display import display_input, display_win, display_loss


def get_random_word():
    """Selects a random word from the list"""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """contains the game loop"""
    # the word to guess
    secret_word = get_random_word()

    # the list that gets filled during the game
    solution_list = []
    for i in range(len(secret_word)):
        solution_list.append("_ ")

    # game state variables
    mistakes = 0
    replaced_letters = 0

    # game loop
    while True:
        guess = display_input(mistakes, solution_list)
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

        # wrong guess
        if not foundLetter:
            mistakes += 1

        # game loss
        if mistakes == MAX_MISTAKES:
            display_loss(mistakes, solution_list)
            break

        # game win
        if replaced_letters == len(secret_word):
            display_win(mistakes, solution_list)
            break
