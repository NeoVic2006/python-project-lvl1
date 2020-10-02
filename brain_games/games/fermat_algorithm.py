import prompt
from random import randint


# Function to print text and check results from fermat_calculations funcion
def fermat_alg():
    count = 3
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print("Answer <yes> if given number is prime. Otherwise answer <no>.")
    while count != 0:
        ans, result = fermat_calculations()
        if ans == "yes":
            if result == 0:
                print("Correct")
            else:
                print("Wrong answer. This number is Not Prime")
        else:
            if result == 0:
                print("Wrong answer. This number is Prime")
            else:
                print("Correct")
        count -= 1
    print("Congratulations, " + name + "!")


# Function to create random number and make 3 Fermat test to check "prime"
# return ans <- User answer
# return result <- test results
def fermat_calculations():
    random_num = randint(3, 1000)
    rand_test_one = randint(2, random_num - 1)
    rand_test_two = randint(2, random_num - 1)
    rand_test_three = randint(2, random_num - 1)

    # Fermat primality test
    result = ((((rand_test_one**random_num) - rand_test_one) % random_num) +
              (((rand_test_two**random_num) - rand_test_two) % random_num) +
              (((rand_test_three**random_num) - rand_test_three) % random_num))

    print("Is this number prime: " + str(random_num))
    ans = prompt.string('Your answer: ')

    return ans, result