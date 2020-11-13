import random

DESCRIPTION = "Find the greatest common divisor of given numbers."
RANDOM_NUMBER_MIN = 1
RANDOM_NUMBER_MAX = 50


def get_question_answer():
    """Function to create 2 random Ints and question info
       Returns result of greatest common divisor   """
    number_one = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    number_two = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    question = "{} {}".format(number_one, number_two)
    answer = search_GCD(number_one, number_two)
    return question, str(answer)


def search_GCD(number_one, number_two):
    while number_one != number_two:
        if number_one > number_two:
            number_one -= number_two
        else:
            number_two -= number_one
    return number_one
