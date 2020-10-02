import prompt
import operator
import random
from random import randint
from brain_games.scripts.add_functions import greetings, comparing_results


# Function to make all calculation and return 2 parameters
def calc_for_calc():
    first_num = randint(0, 100)
    second_num = randint(0, 100)
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul}
    op = random.choice(list(operators.keys()))

    print("Question: " + str(first_num) + str(op) + str(second_num))
    ans = prompt.string('Your answer: ')
    res = operators.get(op)(first_num, second_num)
    return ans, res


# Main function to check and print result
def calculator():
    name_calc = greetings()
    print("What is the result of the expression?")
    for x in range(3):
        ans, res = calc_for_calc()
        comparing_results(ans, res)
    print("Congratulations, " + name_calc + "!")
