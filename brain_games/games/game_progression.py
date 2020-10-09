from random import randint


DESCRIPTION = "What number is missing in the progression?"
RANDOM_NUMB_START = 1
RANDOM_NUMB_END = 1000
RANDOM_STEP_START = 1
RANDOM_STEP_END = 5
HIDE_ELEM_START = 0
HIDE_ELEM_END = 9


# Calculation function which create random Ints,
# printing "fixed" List and return:
# memor_elem <- element which was hidden
def get_game_calculations():
    list_of_num = []
    random_number = randint(RANDOM_NUMB_START, RANDOM_NUMB_END)
    step = randint(RANDOM_STEP_START, RANDOM_STEP_END)
    element_to_hide = randint(HIDE_ELEM_START, HIDE_ELEM_END)
    for _ in range(10):
        random_number += step
        list_of_num.append(random_number)
    elem_to_find = list_of_num[element_to_hide]
    list_of_num[element_to_hide] = ".."
    x = "".join(str(list_of_num))
    x = x.replace(',', ' ')
    question = x.strip('[]')
    return str(elem_to_find), question
