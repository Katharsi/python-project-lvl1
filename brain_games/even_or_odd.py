import prompt

from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_OF_ROUND = 3

def generate_number():
    number = randint(1, 99)
    answer = 'yes' if number % 2 is True else 'no'
    return str(number), answer


def get_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(DESCRIPTION)
    start_round = 1

    for start_round in range(NUMBER_OF_ROUND):
        question, answer = game.generate_number()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(answer):
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct anwer was {answer}."
                  f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
