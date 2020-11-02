import random

DESCRIPTION = "Answer yes if given number is prime. Otherwise answer no."
RANDOM_NUMB_MIN = 3
RANDOM_NUMB_MAX = 1000


# Function to create random number and return result(prime or no)
def get_question_answer():
    random_num = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    result = 'yes' if is_number_prime(random_num) else 'no'
    return result, random_num


# Fermat primality test
def is_number_prime(random_num):
    if random_num // 2 == 0:
        if random_num % 2 == 0:
            return True
    return False
