"""brain-progression game."""
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_ar_progression(start_number, step, length):
    """Generate arithmetic progression."""
    return list(range(start_number, start_number + length * step, step))


def get_random_number():
    """Create past num in getting progression."""
    start_number = randint(1, 50)
    step = randint(1, 25)
    length = 10
    ar_progression = [str(num) for num in generate_ar_progression(
        start_number, step, length)]
    missing_num = randint(0, len(ar_progression) - 1)
    correct_answer = ar_progression[missing_num]
    ar_progression[missing_num] = '..'
    return ' '.join(ar_progression), correct_answer
