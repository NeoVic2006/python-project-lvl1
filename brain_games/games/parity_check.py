import random

DESCRIPTION = "Answer yes if the number is even, otherwise answer no."
RANDOM_NUMB_MIN = 1
RANDOM_NUMB_MAX = 1000


# Function to create random number and return results
def get_question_answer():
    random_num = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    result = 'yes' if random_num % 2 == 0 else 'no'
    return result, random_num


