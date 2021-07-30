"""
    Contains some functions required by other modules
"""
import sys
from os import system
from time import sleep
from .display import LINE


def exit_game() -> None:
    """
        Exit the game!
    """

    print(f"{LINE}\n\t\t\t\t\t\t\t\t\t|Thanks for playing!|\n{LINE}")
    sleep(0.4)
    sys.exit()


def clear_screen() -> int:
    """
        This function uses the system function from os to
        clear the console screen. It passes 'clear' or 'cls'
        as the arguments depending on the OS.
    """

    return system("cls") if sys.__name__ == "nt" else system("clear")
