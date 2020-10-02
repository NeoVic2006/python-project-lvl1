from brain_games.games.nod_algorithm import calc_for_nod
from brain_games.scripts.add_functions import greetings


def main():
    greetings()
    print("Find the greatest common divisor of given numbers.")
    for x in range(3):
        calc_for_nod()


if __name__ == '__main__':
    main()
