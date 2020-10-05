from brain_games.games.game_calculcator import calculator
from brain_games.scripts.add_functions import greetings
from brain_games.games.game_progression import progression
from brain_games.games.nod_algorithm import calc_for_nod
from brain_games.games.fermat_algorithm import fermat_calc


def game_calculator():
    greetings()
    calculator()


def game_progression():
    greetings()
    progression()


def NOD_algorithm():
    greetings()
    print("Find the greatest common divisor of given numbers.")
    for x in range(3):
        calc_for_nod()


def fermat_algorithm():
    greetings()
    fermat_calc()


def main():
    pass


if __name__ == '__main__':
    main()
