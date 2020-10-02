from brain_games.games.game_calculcator import calculator
from brain_games.scripts.add_functions import greetings

def main():
    name = greetings()
    calculator()
    print("Congratulations, " + name + "!")

if __name__ == '__main__':
    main()
