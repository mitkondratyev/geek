current_line = 1
lines_count = 0
try:
    with open("task2.txt") as f_obj:
        for line in f_obj:
            print("Количество слов в",current_line,"строке", len(line.split()))
            current_line += 1
            lines_count += 1
except IOError:
    print("Произошла ошибка ввода-вывода!")

print("Количество строк в файле", lines_count)