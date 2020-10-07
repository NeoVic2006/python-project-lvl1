from random import randint

question = "Answer yes if the number is even, otherwise answer no."


# Function to create random number and calculate if this number == parity
# return yes or no
def get_game_calculations():
    random_num = randint(1, 1000)
    result = random_num % 2
    print("Question: " + str(random_num))
    if result == 0:
        return "yes"
    else:
        return "no"
