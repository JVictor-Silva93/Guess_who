"""
Classes.py
"""
# from random import choice


class Card:
    """Defines a card"""

    def __init__(self, details_dict: dict) -> None:

        # Iterate over the keys of the dictionary and set instance attributes 
        # with dict-keys as their names and dict-values as their values
        for key, value in details_dict.items():
            self.__setattr__(key, value)

    def __repr__(self) -> str:
        return f"Card({self.name!r}, {self.gender!r})"


# class Player:
#     """Model a player"""

#     def __init__(self, cards, is_human=True) -> None:
#         self.cards = cards

#         if not is_human:
#             self.secret_card = choice(self.cards)
#         else:
#             # Call a function to get human player's input
#             pass
    