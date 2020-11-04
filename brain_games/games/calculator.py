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
    op_symbol, op_key = random.choice(list(operators.items()))
    question = "{}{}{}".format(first_number, op_symbol, second_number)
    result = op_key(first_number, second_number)
    return str(result), question
