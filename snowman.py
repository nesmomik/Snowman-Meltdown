from game_display import display_intro
from game_logic import play_game


def main():
    while True:
        display_intro()

        play_game()


if __name__ == "__main__":
    main()
