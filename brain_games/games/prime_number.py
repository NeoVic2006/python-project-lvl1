import random

DESCRIPTION = "Answer yes if given number is prime. Otherwise answer no."
RANDOM_NUMB_MIN = 3
RANDOM_NUMB_MAX = 1000


# Function to create random number and return result(prime or no)
def get_question_answer():
    random_num = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    result = 'yes' if fermat_search(random_num) else 'no'
    return result, random_num


# Fermat primality test
def fermat_search(random_num):
    r_test_one = random.randint(RANDOM_NUMB_MIN, random_num - 1)
    r_test_two = random.randint(RANDOM_NUMB_MIN, random_num - 1)
    r_test_three = random.randint(RANDOM_NUMB_MIN, random_num - 1)
    primal_calc = ((((r_test_one**random_num) - r_test_one) % random_num) +
                   (((r_test_two**random_num) - r_test_two) % random_num) +
                   (((r_test_three**random_num) - r_test_three) % random_num))
    if primal_calc == 0:
        return True
    else:
        return False
