"""brain-progression game."""
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_progression(start_number, step_progression, length_progression):
    """Generating an arithmetic progression with a random skip."""
    result = [start_number]
    i = 0
    while i < length_progression:
        start_number += step_progression
        result.append(start_number)
        i += 1
    return result


def generate_number():
    """Generating an arithmetic progression with a random skip."""
    start_number = randint(1, 99)
    step_progression = randint(1, 99)
    length_progression = randint(1, 10)
    func_progression = get_progression(start_number, step_progression, length_progression)
    index = randint(0, length_progression)
    correct_answer = func_progression[index]
    func_progression[index] = '..'
    game_question = ' '.join(map(str, func_progression))
    return game_question, correct_answer
