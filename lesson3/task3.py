def my_min(*args):
    tmp = args[0]
    for item in args:
        if tmp > item:
            tmp = item
    return tmp

def my_func(a, b, c):
    tmp = [a, b, c]
    value = 0
    min_value = my_min(tmp)
    for item in tmp:
        if item != min_value:
            value = value + item
    return value

print(my_func(1, 2, 3))