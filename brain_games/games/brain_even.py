"""brain-even game."""
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    """
    Checking the number for parity.
    Boolean type - True or False.
    """


    return number % 2 == 0


def generate_number():
    """Creating a question-answer form."""

    game_question = randint(1, 99)
    correct_answer = 'yes' if is_even(game_question) else 'no'
    return game_question, correct_answer
