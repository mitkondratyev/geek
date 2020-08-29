from itertools import cycle

list_1 = [1, 2, 3, 4, 5]
i = 0
for el in cycle(list_1):
    if i == 10:
        break
    else:
        print(el)
        i += 1