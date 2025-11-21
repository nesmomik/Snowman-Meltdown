from game_display import display_intro
from game_logic import play_game, get_max_mistakes


def main():
    max_mistakes = get_max_mistakes()

    while True:
        display_intro(max_mistakes)

        play_game()


if __name__ == "__main__":
    main()
