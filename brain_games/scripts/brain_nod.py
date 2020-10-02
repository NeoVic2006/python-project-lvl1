from brain_games.games.nod_algorithm import calc_for_nod
from brain_games.scripts.add_functions import greetings

def main():
    name = greetings()
    calc_for_nod()
    print("Congratulations, " + name + "!")

if __name__ == '__main__':
    main()
