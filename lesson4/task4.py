import random

list_1 = [random.randint(0, 10) for _ in range(0, 13)]
list_2 = [itm for itm in list_1 if list_1.count(itm) == 1]
print(list_1)
print(list_2)