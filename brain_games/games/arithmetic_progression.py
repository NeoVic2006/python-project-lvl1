import random


DESCRIPTION = "What number is missing in the progression?"
FIRST_PROGRESSION_NUMBER = 1
LAST_PROGRESSION_NUMBER = 1000
RANDOM_STEP_MIN = 1
RANDOM_STEP_MAX = 5
PROGRESSION_LENGTH = 10


def get_question_answer():
    """Main funcion using 2 functions and
       returning elem to find and ask question"""
    elem_to_find, question = gen_question(gen_proression())
    return elem_to_find, question


def gen_proression():
    """Generating new progression list and returning list to main function"""
    beggining_progression = random.randint(FIRST_PROGRESSION_NUMBER,
                                           LAST_PROGRESSION_NUMBER)
    step = random.randint(RANDOM_STEP_MIN, RANDOM_STEP_MAX)
    progression = []
    for element_number in range(PROGRESSION_LENGTH):
        element_number = beggining_progression + (step*element_number)
        progression.append(element_number)
    return progression


def gen_question(gen_progression):
    """Taking list and hiding element in it. Returning elem and question"""
    progression = gen_progression
    hiding_index = random.randint(0, len(progression) - 1)
    answer_element = progression[hiding_index]
    progression[hiding_index] = ".."
    question = " ".join(str(elem) for elem in progression)
    return str(answer_element), question
