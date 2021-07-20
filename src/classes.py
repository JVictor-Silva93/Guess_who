"""
Classes.py
"""
from random import choice

class Card:
    """Defines a card"""

    def __init__(self, 
                 name,
                 gender,
                 eye_color,
                 hair_color,
                 skin_color,
                 is_bald: bool,
                 earrings: bool):

        self.name = name
        self.gender = gender
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.is_bald = is_bald
        self.earrings = earrings
    
    def __repr__(self):
        return f"Card >> {self.name}"


class Player:
    """Model a player"""

    def __init__(self, cards, is_human=True) -> None:
        self.cards = cards

        if not is_human:
            self.secret_card = choice(self.cards)
        else:
            # Call a function to get human player's input
            pass
    