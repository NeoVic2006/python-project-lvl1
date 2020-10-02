from random import randint
import prompt
from brain_games.scripts.add_functions import greetings, comparing_results


# Function to create 2 random Ints and calculate NOD between them.
# and <- User answer
# ran_one <- its a result from NOD calculation between 2 random numbers
def calc_for_nod():
    print("Find the greatest common divisor of given numbers.")
    ran_one = randint(1, 50)
    ran_two = randint(1, 40)
    print("Question: " + str(ran_one) + " " + str(ran_two))
    ans = prompt.string('Your answer: ')

    while ran_one != ran_two:
        if ran_one > ran_two:
            ran_one -= ran_two
        else:
            ran_two -= ran_one
    comparing_results(ans, ran_one)
    


