from random import randint


DESCRIPTION = "What number is missing in the progression?"
RANDOM_NUMB_START = 1
RANDOM_NUMB_END = 1000
RANDOM_STEP_START = 1
RANDOM_STEP_END = 5
HIDE_ELEM_START = 0
HIDE_ELEM_END = 9


# Main funcion using 2 functions and returning elem to find and question
def get_game_calculations():
    elem_to_find, question = hiding_elem(generating_list())
    return elem_to_find, question


# Generating new list and returning list to main function
def generating_list():
    random_number = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    step = randint(RANDOM_STEP_START, RANDOM_STEP_END)
    new_list = []
    elem_in_list = random_number 
    for _ in range(10):
        elem_in_list += step
        new_list.append(elem_in_list)
    return new_list


# Taking list and hiding elemnt in it. Returning elem and question
def hiding_elem(generated_list):
    element_to_hide = randint(HIDE_ELEM_START, HIDE_ELEM_END)
    elem_to_find = generated_list[element_to_hide]
    generated_list[element_to_hide] = ".."
    question = " ".join(str(int) for int in generated_list)
    return str(elem_to_find), question
