from itertools import count

for el in count(3):
    if el > 10:
        break
    elif el % 2 == 0:
        print(el)