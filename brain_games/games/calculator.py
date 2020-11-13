import operator
import random

DESCRIPTION = "What is the result of the expression?"
RANDOM_NUMBER_MIN = 0
RANDOM_NUMBER_MAX = 100


def get_question_answer():
    """Function creating random parameters and calculate them.
       Return result of calculation and question info   """
    first_number = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    second_number = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul}
    math_sign, math_operation = random.choice(list(operators.items()))
    question = "{}{}{}".format(first_number, math_sign, second_number)
    answer = math_operation(first_number, second_number)
    return question, str(answer)
