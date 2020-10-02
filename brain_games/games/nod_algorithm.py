from random import randint
import prompt
from brain_games.scripts.greetings import greetings

# Function to create 2 random Ints and calculate NOD between them.
# and <- User answer
# ran_one <- its a result from NOD calculation between 2 random numbers
def calculation():
    ran_one = randint(1, 50)
    ran_two = randint(1, 40)
    print("Question: " + str(ran_one) + " " + str(ran_two))
    ans = prompt.string('Your answer: ')

    while ran_one != ran_two:
        if ran_one > ran_two:
            ran_one -= ran_two
        elif ran_two > ran_one:
            ran_two -= ran_one
    return ans, ran_one


# Main function which comparing data from Calculation function and print result
def nod_calculation():
    count = 3
    name = greetings()
    print("Find the greatest common divisor of given numbers.")

    while count != 0:
        ans, ran_one = calculation()
        if int(ans) == ran_one:
            print("Correct")
        else:
            print(ans + " is wrong answer. Correct answer was " + str(ran_one))
            print("Let's try again, " + name + "!")
        count -= 1
    print("Congratulations, " + name + "!")
