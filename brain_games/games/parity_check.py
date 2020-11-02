import random

DESCRIPTION = "Answer yes if the number is even, otherwise answer no."
RANDOM_NUMB_MIN = 1
RANDOM_NUMB_MAX = 1000


# Function to create random number and return results
def get_question_answer():
    random_num = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    if random_num % 2 == 0:
        result = "yes"
    else:
        result = "no"
    return result, random_num
