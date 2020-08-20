from math import factorial

def fact(n):
    for el in range(1, n+1):
        yield factorial(el)

n = 4
for el in fact(n):
    print(el)