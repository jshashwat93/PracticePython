import random


def set_method(my_list):
    print(list(set(my_list)))


def loop_method(my_list):
    new_list = []
    for eachItem in my_list:
        if eachItem not in new_list:
            new_list.append(eachItem)
    print(new_list)


a = [random.randrange(1, 11) for eachItem in range(1, 11)]
set_method(a)
loop_method(a)
