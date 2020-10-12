from random import randint

DESCRIPTION = "Answer yes if given number is prime. Otherwise answer no."
RANDOM_NUMB_START = 3
RANDOM_NUMB_END = 1000


# Function to create random number and make 3 Fermat test to check "prime"
# return yes or no, depends if random number is prime
def get_game_calculations():
    random_num = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    r_test_one = randint(RANDOM_NUMB_START, random_num - 1)
    r_test_two = randint(RANDOM_NUMB_START, random_num - 1)
    r_test_three = randint(RANDOM_NUMB_START, random_num - 1)
    return fermat_search(random_num,
                         r_test_one,
                         r_test_two,
                         r_test_three), random_num


# Fermat primality test
def fermat_search(random_num, r_test_one, r_test_two, r_test_three):
    result = ((((r_test_one**random_num) - r_test_one) % random_num) +
              (((r_test_two**random_num) - r_test_two) % random_num) +
              (((r_test_three**random_num) - r_test_three) % random_num))
    if result == 0:
        return "yes"
    else:
        return "no"
