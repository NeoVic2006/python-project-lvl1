from brain_games.games.fermat_algorithm import fermat_calc
from brain_games.scripts.add_functions import greetings


def main():
    name = greetings()
    fermat_calc()
    print("Congratulations, " + name + "!")

if __name__ == '__main__':
    main()
