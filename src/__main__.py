"""
    Title: Guess Who [Human VS Computer]
    Contributors: Check on GitHub
"""
import sys
from os import system
from time import sleep
from .display import MENU


# Gloabal Variables
LINE = "=" * 66


# TODO: Complete below functions


def start_game(): ...
def show_tutorial(): ...
def show_credits(): ...


def exit_game():
    """Exit the game!"""

    print(f"Thanks for playing!\n{LINE}")
    sleep(0.4)
    sys.exit()


def clear_screen():
    """
        This function uses the system function from os to
        clear the console screen. It passes 'clear' or 'cls'
        as the arguments depending on the OS.
    """

    return system("cls") if sys.__name__ == "nt" else system("clear")


def main():
    """Main function"""

    first_option = "Start Game"
    funcs = [start_game,
             show_tutorial,
             show_credits,
             exit_game]

    while True:
        clear_screen()
        print(MENU.format(first_option))
        option = input("Choose an option >>> ")

        if option in ("1", "2", "3", "4"):

            # If player chose the first option, modify the first option of
            # the menu screen to show 'Play Again' instead of 'Start Game'.
            # This saves us from creating 'play_again' function!
            if option == "1":
                first_option = "Play Again"

            # Call the desired function
            funcs[int(option) - 1]()

        else:
            print(f"Invalid Option!\n{LINE}")
            sleep(0.4)


if __name__ == "__main__":
    main()
