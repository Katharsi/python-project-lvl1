#!/usr/bin/env python
import prompt

from random import randint


NUMBER_OF_ROUND = 3

print('Welcome to the Brain Games!')  
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')

print('Answer "yes" if the number is even, otherwise answer "no".')
start_round = 1

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
