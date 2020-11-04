import random

DESCRIPTION = "Answer yes if the number is even, otherwise answer no."
RANDOM_NUMBER_MIN = 1
RANDOM_NUMBER_MAX = 1000


def get_question_answer():
    """Function to create random number and return results"""
    random_num = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    result = 'yes' if random_num % 2 == 0 else 'no'
    return result, random_num
