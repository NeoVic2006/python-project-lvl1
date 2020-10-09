from random import randint

DESCRIPTION = "Answer yes if the number is even, otherwise answer no."
RANDOM_NUMB_START = 1
RANDOM_NUMB_END = 1000


# Function to create random number and return results 
def get_game_calculations():
    random_num = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    return parity_search(random_num)


# Function to calculate if random number even or odd
def parity_search(random_num):
    result = random_num % 2
    if result == 0:
        return "yes", random_num
    return "no", random_num
