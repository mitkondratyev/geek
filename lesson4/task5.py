import random
from functools import reduce

def my_func(prev_el, el):
    return prev_el * el

list_1 = [itm for itm in range(100, 1001) if itm % 2 == 0]
print(list_1)
print(reduce(my_func, list_1))
