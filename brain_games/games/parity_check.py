import random

DESCRIPTION = "Answer yes if the number is even, otherwise answer no."
RANDOM_NUMB_MIN = 1
RANDOM_NUMB_MAX = 1000


# Function to create random number and return results
def get_question_answer():
    random_num = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    result = check_odd_or_even(random_num)
    return result, random_num


# Function to check if number odd or even and return result
def check_odd_or_even(random_num):
    parity_check = random_num % 2
    if parity_check == 0:
        return "yes"
    return "no"
