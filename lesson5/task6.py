def replace_all(text, dic):
    for r in dic:
        text = text.replace(*r)
    return text

dict = {}
changes = ((":", ""), ("(л)", ""), ("(пр)", ""), ("(лаб)", ""), ("—", "0"))
try:
    with open("task6.txt") as f_obj:
        for line in f_obj:
            name, lections, practics, labs = line.split()
            name = replace_all(name, changes)
            lections = int(replace_all(lections, changes))
            practics = int(replace_all(practics, changes))
            labs = int(replace_all(labs, changes))
            dict[name] = lections + practics + labs
except IOError:
    print("Произошла ошибка ввода-вывода!")

print(dict)
