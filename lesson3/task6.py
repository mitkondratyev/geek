def int_func(str):
    return str.capitalize()

def all_int_func(str):
    tmp = str.split()
    tmp = [int_func(word) for word in tmp]
    return ' '.join(tmp)


print(int_func('text'))
print(all_int_func('all text to capitalize'))