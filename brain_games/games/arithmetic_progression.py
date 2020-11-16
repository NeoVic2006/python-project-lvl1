import random


DESCRIPTION = "What number is missing in the progression?"
MIN_PROGRESSION_NUMBER = 1
MAX_PROGRESSION_NUMBER = 1000
RANDOM_STEP_MIN = 1
RANDOM_STEP_MAX = 5
PROGRESSION_LENGTH = 10


def gen_proression(begining_progression, step, progression_length):
    """Generating new progression list and returning list to main function"""
    progression = []
    for element_number in range(progression_length):
        element_number = begining_progression + (step*element_number)
        progression.append(element_number)
    return progression


def get_question_answer():
    """Taking list and hiding element in it. Returning elem and question"""
    begining_progression = random.randint(MIN_PROGRESSION_NUMBER,
                                          MAX_PROGRESSION_NUMBER)
    step = random.randint(RANDOM_STEP_MIN, RANDOM_STEP_MAX)
    progression = gen_proression(begining_progression, step, PROGRESSION_LENGTH)
    hiding_index = random.randint(0, len(progression) - 1)
    answer = progression[hiding_index]
    progression[hiding_index] = ".."
    question = " ".join(str(elem) for elem in progression)
    return question, str(answer)
