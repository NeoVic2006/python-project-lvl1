import random


DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_NUMBER_MIN = 1
PROGRESSION_NUMBER_MAX = 1000
RANDOM_STEP_MIN = 1
RANDOM_STEP_MAX = 5
PROGRESSION_LENGTH = 10


def get_question_answer():
    '''Main funcion using 2 functions and
       returning elem to find and ask question'''
    elem_to_find, question = gen_question(gen_proression())
    return elem_to_find, question


def gen_proression():
    '''Generating new progression list and returning list to main function'''
    random_number = random.randint(PROGRESSION_NUMBER_MIN,
                                   PROGRESSION_NUMBER_MAX)
    step = random.randint(RANDOM_STEP_MIN, RANDOM_STEP_MAX)
    progression = []
    for element in range(PROGRESSION_LENGTH):
        element = random_number + (step*element)
        progression.append(element)
    return progression


def gen_question(generated_list):
    '''Taking list and hiding elemnt in it. Returning elem and question'''
    element_to_hide = random.randint(0, PROGRESSION_LENGTH)
    elem_to_find = generated_list[element_to_hide]
    generated_list[element_to_hide] = ".."
    question = " ".join(str(elem) for elem in generated_list)
    return str(elem_to_find), question
