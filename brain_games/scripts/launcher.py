import prompt


NUMBER_OF_ROUNDS = 3


# Main function to Welcome user,
# ask question and request function to Compare results
def launcher(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(user_name))
    print(game.DESCRIPTION)
    running_game_cicles(game.get_question_answer, user_name)


# Function receiveing username and calculation function from proper game.
# comparing user and calculation function results and print it
def running_game_cicles(calc_function, user_name):
    for _ in range(NUMBER_OF_ROUNDS):
        correct_answer, question = calc_function()
        print("Question: {}" .format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print("Correct")
        else:
            print("{} is wrong answer. Correct answer was {}"
                  .format(user_answer, correct_answer))
            print("Let's try again, {}".format(user_name))
    print("Congratulations, {}!".format(user_name))
