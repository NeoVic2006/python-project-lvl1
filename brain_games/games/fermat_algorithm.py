from random import randint

question = "Answer yes if given number is prime. Otherwise answer no."


# Function to create random number and make 3 Fermat test to check "prime"
# return yes or no, depends if random number is prime
def get_game_calculations():
    random_num = randint(3, 1000)
    r_test_one = randint(2, random_num - 1)
    r_test_two = randint(2, random_num - 1)
    r_test_three = randint(2, random_num - 1)

    # Fermat primality test
    result = ((((r_test_one**random_num) - r_test_one) % random_num) +
              (((r_test_two**random_num) - r_test_two) % random_num) +
              (((r_test_three**random_num) - r_test_three) % random_num))
    print("Is this number prime: " + str(random_num))

    if result == 0:
        return "yes"
    else:
        return "no"
