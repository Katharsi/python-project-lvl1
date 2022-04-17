"""brain-calc game."""
from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'
OPERATOR = ['+', '-', '*']


def generate_number_equation():
    """Generate math random number and operator."""
    number_one = randint(1, 99)
    number_two = randint(1, 99)
    operator = choice(OPERATOR)
    game_question = f'{number_one} {operator} {number_two}'
    if operator == '+':
        correct_answer = str(number_one + number_two)
        return game_question, correct_answer
    elif operator == '-':
        correct_answer = str(number_one - number_two)
        return game_question, correct_answer
    correct_answer = str(number_one * number_two)
    return game_question, correct_answer
