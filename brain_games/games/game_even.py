import random

DESCRIPTION = "Answer yes if the number is even, otherwise answer no."
RANDOM_NUMBER_MIN = 1
RANDOM_NUMBER_MAX = 1000


def get_question_answer():
    """Function to create random number and return results"""
    question = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
