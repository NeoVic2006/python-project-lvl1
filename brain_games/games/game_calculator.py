import operator
import random
from random import randint

question = "What is the result of the expression?"


# Function creating random parameters and calculate them.
# Return result of calculation
def get_game_calculations():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul}
    op_keys = random.choice(list(operators.keys()))
    print("Question: " + str(first_number) + str(op_keys) + str(second_number))
    result = operators.get(op_keys)(first_number, second_number)
    return result
