import prompt

from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_OF_ROUND = 3
start_round = 1

def get_game():
    print('Welcome to the Brain Games!')  
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(DESCRIPTION)
    for start_round in range(NUMBER_OF_ROUND): 
        number = randint(1, 99)
        print(f'Question: {number}')
    
        answer = prompt.string('Your answer: ')
        if answer == 'yes':
            if number % 2 == 0:
                print('Correct!')
            elif number % 2 != 0:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                      f"Let's try again, {name}!")
        elif answer == 'no':
            if number % 2 != 0:
                print('Correct!')
            elif number % 2 == 0:
                print(f"'no' is wrong answer ;(. Correct anwer was 'yes'."
                      f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
