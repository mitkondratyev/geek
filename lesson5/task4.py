def replace_all(text, dic):
    for r in dic:
        text = text.replace(*r)
    return text

changes = (("1", "один"), ("2", "два"), ("3", "три"), ("4", "четыре"))
try:
    with open("task4_in.txt") as f_obj:
        for line in f_obj:
            line = replace_all(line, changes)
            f_obj = open("task4_out.txt", 'a')
            f_obj.write(line)
            f_obj.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")