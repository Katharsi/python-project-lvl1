import prompt

from random import randint, choice


ROUNDS = 3
DESCRIPTION = 'What is the result of the expression?'
OPERATOR = ['+', '-', '*']


def calc(number_one, operators, number_two):
    if operators == '+':
        return number_one + number_two
    if operators == '-':
        return number_one - number_two
    if operators == '*':
        return number_one * number_two


def generate_operation():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(DESCRIPTION)
    for start in range(ROUNDS):
        number_one = randint(1, 99)
        number_two = randint(1,99)
        operators = choice(OPERATOR)
        question = f'{number_one} {operators} {number_two}'
        print(f'Question: {question}')
        answer = calc(number_one, operators, number_two)
        user_answer = prompt.string('Your answer: ')
        if user_answer:
            if answer == user_answer:
                print('Correct!')
            else:
                print(f"{str(user_answer)} is wrong answer ;(. Correct answer was {str(answer)}.")
                print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
