from random import randint

DESCRIPTION = "Answer yes if the number is even, otherwise answer no."
RANDOM_NUMB_START = 1
RANDOM_NUMB_END = 1000


# Function to create random number and return results
def get_game_calculations():
    random_num = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    result = check_odd_or_even(parity_search(random_num))
    return result, random_num


# Function to calculate number
def parity_search(random_num):
    parity_calc = random_num % 2
    return parity_calc


# Function to check if number odd or even and return result
def check_odd_or_even(parity_calc):
    if parity_calc == 0:
        return "yes"
    return "no"
