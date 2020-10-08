import prompt


NUMBER_OF_ROUNDS = 3


# Main function to Welcome user,
# ask question and request function to Compare results
def game_launch(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print("Hello, " + user_name + "!")
    print(game.question)
    comparing_results(game.get_game_calculations, user_name)


# Function receiveing username and calculation function from proper game.
# comparing user and calculation function results and print it
def comparing_results(calc_function, user_name):
    for _ in range(NUMBER_OF_ROUNDS):
        correct_answer = calc_function()
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(user_answer + " is wrong answer. Correct answer was "
                  + str(correct_answer))
            print("Let's try again, " + user_name)
        else:
            print("Correct")
    print("Congratulations, " + user_name + "!")
