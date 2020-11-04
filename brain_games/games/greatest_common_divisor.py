import random

DESCRIPTION = "Find the greatest common divisor of given numbers."
RANDOM_NUMBER_MIN = 1
RANDOM_NUMBER_MAX = 50


def get_question_answer():
    """Function to create 2 random Ints and question info
       Returns result of greatest common divisor   """
    random_number_one = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    random_number_two = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    question = "{} {}".format(random_number_one, random_number_two)
    correct_GCD_numb = search_GCD(random_number_one, random_number_two)
    return str(correct_GCD_numb), question


def search_GCD(number_one, number_two):
    while number_one != number_two:
        if number_one > number_two:
            number_one -= number_two
        else:
            number_two -= number_one
    return number_one
