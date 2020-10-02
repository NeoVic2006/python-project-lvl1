import prompt


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    return name


def comparing_results(ans, result):
    if int(ans) == result:
        print("Correct")
    else:
        print(ans + " is wrong answer. Correct answer was " + str(result))
