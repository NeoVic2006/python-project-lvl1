import random

DESCRIPTION = "Find the greatest common divisor of given numbers."
RANDOM_NUMB_MIN = 1
RANDOM_NUMB_MAX = 50


# Function to create 2 random Ints and question info
# Returns result of greatest common divisor
def get_question_answer():
    random_one = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    random_two = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    question = "{} {}".format(random_one, random_two)
    correct_GCD_numb = search_GCD(random_one, random_two)
    return str(correct_GCD_numb), question


def search_GCD(number_one, number_two):
    while number_one != number_two:
        if number_one > number_two:
            number_one -= number_two
        else:
            number_two -= number_one
    return number_one
