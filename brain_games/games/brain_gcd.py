"""brain-gcd game."""
from math import gcd
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_number():
    """Generate random numbers and find the largest divisor."""
    number_one = randint(1, 99)
    number_two = randint(1, 99)
    game_question = f'{number_one} {number_two}'
    correct_answer = gcd(number_one, number_two)
    return game_question, correct_answer
   