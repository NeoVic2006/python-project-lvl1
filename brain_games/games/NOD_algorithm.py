from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers."
RANDOM_NUMB_START = 1
RANDOM_NUMB_END = 50


# Function to create 2 random Ints and question info
# Returns result of NOD_search calculations
def get_game_calculations():
    random_one = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    random_two = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    question = str(random_one) + " " + str(random_two)
    return search_NOD(random_one, random_two), question


# Getting 2 random number and searching for NOD
# Returns NOD
def search_NOD(random_one, random_two):
    while random_one != random_two:
        if random_one > random_two:
            random_one -= random_two
        else:
            random_two -= random_one
    return str(random_one)
