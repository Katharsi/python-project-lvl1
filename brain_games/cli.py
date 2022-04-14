import prompt


def get_welcome_username():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    
def get_answer_user():
    answer = prompt.string('Your answer: ')
