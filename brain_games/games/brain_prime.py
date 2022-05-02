"""brain-prime game."""
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """Get prime number."""
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    if count <= 0:
        return True
    else:
        return False


def get_random_number():
    """Creating a question-answer form."""
    number = randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    game_question = f'Question: {number}'
    return game_question, correct_answer
