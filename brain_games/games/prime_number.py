import random

DESCRIPTION = "Answer yes if given number is prime. Otherwise answer no."
RANDOM_NUMBER_MIN = 2
RANDOM_NUMBER_MAX = 100


def get_question_answer():
    """Function to create random number and return result(prime or no)"""
    random_num = random.randint(RANDOM_NUMBER_MIN, RANDOM_NUMBER_MAX)
    answer = 'yes' if is_prime(random_num) else 'no'
    return random_num, answer


def is_prime(number):
    """Checking if number is prime or not"""
    if number < 2:
        return False
    max_divider_possible = number // 2
    for divider in range(2, max_divider_possible):
        if number % divider == 0:
            return False
    return True
