"""brain-calc game."""
import operator

from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_random_number():
    """Generate math random number and operator."""
    number_one = randint(0, 100)
    number_two = randint(1, 100)
    operator = choice(list(operators.keys()))
    game_question = f'{number_one} {operator} {number_two}'
    correct_answer = get_correct_answer(number_one, operator, number_two)
    return game_question, correct_answer


def get_correct_answer(number_one, operator, number_two):
    """Get programm correct_answer."""
    return str(operators[operator](number_one, number_two))
