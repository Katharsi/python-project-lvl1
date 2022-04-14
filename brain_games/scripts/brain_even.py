from random import randint

from brain_games.cli import get_welcome_username, get_answer_user


def greeting():
    username = get_welcome_username()
    return username