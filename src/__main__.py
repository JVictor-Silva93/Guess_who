"""
    Title: Guess Who [Human VS Computer]
    Contributors: Check on GitHub

    Guess Who? is a classic fun game for two players.
"""

import json
from time import sleep
from .display import (LINE,
                      show_cards,
                      show_questions,
                      show_menu,
                      show_about_page,
                      show_credits_page)
from .helper import (clear_screen,
                     exit_game)
from .classes import Player

##################################################################
# Import cards from cards.json and questions from questions.json
##################################################################
with open("Data/cards.json") as cards_json:
    cards_list = json.load(cards_json)

with open("Data/questions.json") as questions_json:
    questions_list = json.load(questions_json)
##################################################################


def start_game():
    """
        Handle the game
    """
    ########################################################
    # The below function call is just for testing purpose
    ########################################################
    player = Player(questions=questions_list[:],
                    cards=cards_list[:],
                    secret_card=cards_list[0])

    show_cards(player)
    show_questions(player)
    input()
    ########################################################


def main() -> None:
    """Main function"""

    first_option = "Start Game"
    funcs = [start_game,
             show_about_page,
             show_credits_page,
             exit_game]

    while True:
        clear_screen()
        show_menu(first_option=first_option)
        option = input("Choose an option >>> ")

        if option in ("1", "2", "3", "4"):

            # If player chose the first option, modify the first option of
            # the menu screen to show 'Play Again' instead of 'Start Game'.
            # This saves us from creating 'play_again' function!
            if option == "1":
                first_option = "Play Again"

            # Clear screen and call the desired function
            clear_screen()
            funcs[int(option) - 1]()

        else:
            print(f"Invalid Option!\n{LINE}")
            sleep(0.4)


if __name__ == "__main__":
    main()
