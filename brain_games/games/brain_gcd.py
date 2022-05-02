"""brain-gcd game."""
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_number():
    """Generate random numbers and find the largest divisor."""
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    game_question = f'{number_one} {number_two}'
    correct_answer = gcd(number_one, number_two)
    return game_question, str(correct_answer)


def gcd(number_one, number_two):
    """Generate GCD function, using the recursion."""
    if number_two == 0:
        return number_one
    else:
        return gcd(number_two, number_one % number_two)
