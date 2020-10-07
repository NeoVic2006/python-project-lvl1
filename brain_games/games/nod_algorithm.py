from random import randint

question = "Find the greatest common divisor of given numbers."


# Function to create 2 random Ints and calculate NOD between them.
# random_one <- its a result from NOD calculation between 2 random numbers
def get_game_calculations():
    random_one = randint(1, 50)
    random_two = randint(1, 40)
    print("Question: " + str(random_one) + " " + str(random_two))

    while random_one != random_two:
        if random_one > random_two:
            random_one -= random_two
        else:
            random_two -= random_one
    return random_one
