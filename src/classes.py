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


class Player:
    """Model a player"""

    def __init__(self,
                 questions: list,
                 cards: list,
                 secret_card: Card) -> None:

        self.questions = questions
        self.cards = cards
        self.secret_card = secret_card

    def remove_question(self, id: int) -> dict:
        """
            Remove the question with param: id from the cards attribute
        """

        for question in self.questions:
            if question["id"] == id:
                return self.questions.pop(self.questions.index(question))

        return {}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{tuple(vars(self))}"
