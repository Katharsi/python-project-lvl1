"""Base template for running games."""
import prompt


def welcome_user():
    """Get username, greeting his\her and return getting username."""

    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


def get_answer_user():
    """Getting an answer to the question posed."""

    user_answer = prompt.string('Your answer: ')
    return user_answer


def run_game(game, game_rounds=3):
    """Run base menu game."""

    username = welcome_user()
    print(game.DESCRIPTION)
    while game_rounds:
        game_question, correct_answer = game.generate_number()
        print(f'Question: {game_question}')
        user_answer = get_answer_user()
        print(user_answer)
        if user_answer == correct_answer:
            print('Correct!')
            game_rounds -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'"/
                  f"Let's try again, {username}!")
            break
    if not game_rounds:
        print(f'Congratulations, {username}!')
