import operator
import random

DESCRIPTION = "What is the result of the expression?"
RANDOM_NUMB_MIN = 0
RANDOM_NUMB_MAX = 100


# Function creating random parameters and calculate them.
# Return result of calculation and question info
def get_question_answer():
    first_number = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    second_number = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul}
    op_keys = random.choice(list(operators.keys()))
    question = "{}{}{}".format(first_number, op_keys, second_number)
    result = operators.get(op_keys)(first_number, second_number)
    return str(result), question
