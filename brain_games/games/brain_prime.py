"""brain-prime game."""
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_number(number):
    """Get prime number."""
    if number < 2:
        return False
    i = 2
    while i <= number // 2:
        if number % i == 0:
            return False
        i += 1
    return True


def generate_number():
    """Creating a question-answer form."""
    number = randint(1, 99)
    correct_answer = 'yes' if prime_number(number) else 'no'
    game_question = f'Question: {number}'
    return game_question, correct_answer
