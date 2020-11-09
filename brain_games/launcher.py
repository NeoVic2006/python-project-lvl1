import prompt


NUMBER_OF_ROUNDS = 3


def launch(game):
    """Main function to Welcome user,
       ask question and request function to Compare results"""
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(user_name))
    print(game.DESCRIPTION)
    run_game_loop(game.get_question_answer, user_name)


def run_game_loop(generate_question_answer, user_name):
    """Function receiveing username and calculation function from proper game.
         comparing user and calculation function results and print it      """
    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = generate_question_answer()
        print("Question: {}" .format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print("{} is wrong answer. Correct answer was {}"
                  .format(user_answer, correct_answer))
            print("Let's try again, {}".format(user_name))
            return
        print("Correct")
    print("Congratulations, {}!".format(user_name))
