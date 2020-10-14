import random

DESCRIPTION = "Find the greatest common divisor of given numbers."
RANDOM_NUMB_MIN = 1
RANDOM_NUMB_MAX = 50


# Function to create 2 random Ints and question info
# Returns result of greatest common divisor
def get_question_answer():
    random_one = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    random_two = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    question = "{} {}".format(random_one, random_two)
    correct_Nod_numb = search_NOD(random_one, random_two)
    return str(correct_Nod_numb), question


def search_NOD(numb_one, numb_two):
    while numb_one != numb_two:
        if numb_one > numb_two:
            numb_one -= numb_two
        else:
            numb_two -= numb_one
    return numb_one
