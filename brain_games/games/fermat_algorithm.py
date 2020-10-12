from random import randint

DESCRIPTION = "Answer yes if given number is prime. Otherwise answer no."
RANDOM_NUMB_START = 3
RANDOM_NUMB_END = 1000


# Function to create random number and return result(prime or no) 
def get_game_calculations():
    random_num = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    result = checking_if_prime(fermat_search(random_num))
    return result, random_num


# Fermat primality test
def fermat_search(random_num):
    r_test_one = randint(RANDOM_NUMB_START, random_num - 1)
    r_test_two = randint(RANDOM_NUMB_START, random_num - 1)
    r_test_three = randint(RANDOM_NUMB_START, random_num - 1)
    primality_calc = ((((r_test_one**random_num) - r_test_one) % random_num) +
                      (((r_test_two**random_num) - r_test_two) % random_num) +
                      (((r_test_three**random_num) - r_test_three) % random_num))
    return primality_calc


# Checking if number is Prime
def checking_if_prime(primality_calc):
    if primality_calc == 0:
        return "yes"
    else:
        return "no"
