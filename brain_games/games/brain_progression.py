"""brain-progression game."""
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_progression(start_number, step_progression, length_progression):
    """Generating an arithmetic progression with a random skip."""
    return list(range(start_number,
                      start_number + length_progression * step_progression,
                      step_progression))


def generate_number():
    """Generating an arithmetic progression with a random skip."""
    start_number = randint(1, 99)
    step_progression = randint(1, 99)
    length_progression = 10
    func_progression = [str(num) for num in get_progression(start_number,
                                                            step_progression,
                                                            length_progression)]
    missing_num = randint(0, len(func_progression) - 1)
    correct_answer = func_progression[missing_num]
    func_progression[missing_num] = '..'
    return ' '.join(func_progression), correct_answer
