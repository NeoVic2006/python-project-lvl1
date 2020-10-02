from brain_games.games.game_progression import preogression
from brain_games.scripts.add_functions import greetings

def main():
    name = greetings()
    preogression()
    print("Congratulations, " + name + "!")

if __name__ == '__main__':
    main()
