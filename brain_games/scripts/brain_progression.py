#!/usr/bin/env python
from brain_games.base_brain import run_game
from brain_games.games import brain_progression


def main():
    """Run main function."""
    run_game(brain_progression)


if __name__ == '__main__':
    main()
