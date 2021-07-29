"""
Classes.py
"""


class Card:
    """Defines a card"""

    def __init__(self, details_dict: dict) -> None:
        "Initialize card and set attributes"

        # Iterate over the keys of the dictionary and set instance attributes
        # with dict-keys as their names and dict-values as their values
        for key, value in details_dict.items():
            self.__setattr__(key, value)

    def __repr__(self) -> str:
        "Return the printable representation of a card"

        return f"{self.__class__.__name__}({vars(self)})"
