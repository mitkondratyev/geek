def my_func(x, y):
    return x**y

def my_func2(x, y):
    tmp = 1
    while y < 0:
        tmp = tmp/x
        y = y+1
    return tmp

print(my_func2(2, -1))