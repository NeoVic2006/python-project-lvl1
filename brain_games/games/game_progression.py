from random import randint


question = "What number is missing in the progression?"


# Calculation function which create random Ints,
# printing "fixed" List and return:
# memor_elem <- element which was hidden
def get_game_calculations():
    list_of_num = []
    random_number = randint(1, 100)
    step = randint(1, 5)
    element_to_hide = randint(0, 9)

    for _ in range(10):
        random_number += step
        list_of_num.append(random_number)

    elem_to_find = list_of_num[element_to_hide]
    list_of_num[element_to_hide] = ".."
    list_of_num = str(list_of_num).strip('[]')
    print("Question: " + list_of_num.replace(',', ''))
    return elem_to_find
