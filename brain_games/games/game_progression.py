from random import randint
import prompt
from brain_games.scripts.add_functions import comparing_results


# Calc function which create random Ints, printing "cleaned" List and return:
# ans <- user answer,
# memor_elem <- element which was hidden
def progression():
    print("What number is missing in the progression?")
    for x in range(3):
        list_of_num = []
        random_num = randint(1, 100)
        step = randint(1, 5)
        find_element = randint(0, 9)

        for x in range(10):
            random_num = random_num + step
            list_of_num.append(random_num)\

        memor_elem = list_of_num[find_element]
        list_of_num[find_element] = ".."
        list_of_num = str(list_of_num).strip('[]')
        print("Question: " + list_of_num.replace(',', ''))
        ans = prompt.string('Your answer: ')
        comparing_results(ans, memor_elem)
