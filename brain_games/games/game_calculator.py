import operator
import random
from random import randint

DESCRIPTION = "What is the result of the expression?"
RANDOM_NUMB_START = 0
RANDOM_NUMB_END = 100


# Function creating random parameters and calculate them.
# Return result of calculation and question info 
def get_game_calculations():
    first_number = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    second_number = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul}
    op_keys = random.choice(list(operators.keys()))
    question = str(first_number) + str(op_keys) + str(second_number)
    result = operators.get(op_keys)(first_number, second_number)
    return str(result), question
