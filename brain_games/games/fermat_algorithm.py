import prompt
from random import randint


# Function to create random number and make 3 Fermat test to check "prime"
# return ans <- User answer
# return result <- test results
def fermat_calc():
    print("Answer yes if given number is prime. Otherwise answer no.")
    for x in range(3):
        random_num = randint(3, 1000)
        r_test_one = randint(2, random_num - 1)
        r_test_two = randint(2, random_num - 1)
        r_test_three = randint(2, random_num - 1)

        # Fermat primality test
        result = ((((r_test_one**random_num) - r_test_one) % random_num) +
                  (((r_test_two**random_num) - r_test_two) % random_num) +
                  (((r_test_three**random_num) - r_test_three) % random_num))

        print("Is this number prime: " + str(random_num))
        ans = prompt.string('Your answer: ')
        checking_answers(ans, result)


def checking_answers(ans, result):
    if (result == 0 and ans == "yes") or (result > 0 and ans == "no"):
        print("Correct")
    else:
        print("Wrong answer.")
