"""brain-even game."""
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_random_number():
    """Creating a question-answer form."""

    game_question = randint(0, 100)
    correct_answer = 'yes' if game_question % 2 == 0 else 'no'
    return game_question, correct_answer
