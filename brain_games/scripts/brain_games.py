from brain_games.games import game_calculator
from brain_games.games import game_progression
from brain_games.games import game_parity
from brain_games.games import NOD_algorithm
from brain_games.games import fermat_algorithm
from brain_games.scripts.add_functions import game_launch


def start_calculator_game():
    game_launch(game_calculator)


def start_progression_game():
    game_launch(game_progression)


def start_NOD_algorithm():
    game_launch(NOD_algorithm)


def start_fermat_algorithm():
    game_launch(fermat_algorithm)


def start_parity_game():
    game_launch(game_parity)


def main():
    pass


if __name__ == '__main__':
    main()
