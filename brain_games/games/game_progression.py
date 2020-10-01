import random
from random import randint




def progression():
    list_of = []
    random_num= randint(1, 100)
    step = randint(1, 5)

    for x in range(10):
        list_of.append(random_num + step)
    print(list_of)