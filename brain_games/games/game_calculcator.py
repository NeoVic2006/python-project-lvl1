import prompt
import operator
import random
from random import randint
from brain_games.scripts.greetings import greetings

# Function to make all calculation and return 2 parameters
def calculations():
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
    count = 3
    name = greetings()
    print("What is the result of the expression?")

    while count != 0:
        ans, res = calculations()
        if int(ans) == res:
            print("Correct")
        else:
            print(ans + " is wrong answer. Correct answer was " + str(res))
            print("Let's try again, " + name + "!")
        count -= 1
    print("Congratulations, " + name + "!")
