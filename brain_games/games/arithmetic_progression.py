import random


DESCRIPTION = "What number is missing in the progression?"
RANDOM_NUMB_MIN = 1
RANDOM_NUMB_MAX = 1000
RANDOM_STEP_START = 1
RANDOM_STEP_END = 5
LIST_LENGTH = 10


# Main funcion using 2 functions and returning elem to find and question
def get_question_answer():
    elem_to_find, question = gen_question(gen_proression())
    return elem_to_find, question


# Generating new progression list and returning list to main function
def gen_proression():
    random_number = random.randint(RANDOM_NUMB_MIN, RANDOM_NUMB_MAX)
    step = random.randint(RANDOM_STEP_START, RANDOM_STEP_END)
    progression_list = []
    elem_in_list = random_number
    for _ in range(LIST_LENGTH):
        elem_in_list += step
        progression_list.append(elem_in_list)
    return progression_list


# Taking list and hiding elemnt in it. Returning elem and question
def gen_question(generated_list):
    element_to_hide = random.randint(0, LIST_LENGTH)
    elem_to_find = generated_list[element_to_hide]
    generated_list[element_to_hide] = ".."
    question = " ".join(str(elem) for elem in generated_list)
    return str(elem_to_find), question
