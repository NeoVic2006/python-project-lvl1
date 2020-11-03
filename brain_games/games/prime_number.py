import random

DESCRIPTION = "Answer yes if given number is prime. Otherwise answer no."
RANDOM_NUMBER_MIN = 2
RANDOM_NUMBER_MAX = 100


def get_question_answer():
    '''Function to create random number and return result(prime or no)'''
    random_num = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    result = 'yes' if is_number_prime(random_num) else 'no'
    return result, random_num


def is_number_prime(random_num):
    '''Checking if number is prime or not'''
    devider = random_num // 2
    for element in range(2, devider):
        if random_num % element == 0:
            return False
    return True
