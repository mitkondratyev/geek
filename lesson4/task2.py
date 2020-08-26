import random

list_1 = [random.randint(0, 300) for _ in range(0, 13)]
list_2 = [itm for idx, itm in enumerate(list_1) if idx < len(list_1) - 1 and list_1[idx] > list_1[idx + 1]]
print(list_1)
print(list_2)