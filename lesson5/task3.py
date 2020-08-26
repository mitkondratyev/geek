less_then_20k = []
all_salary = 0
count = 0
try:
    with open("task3.txt") as f_obj:
        for line in f_obj:
            tmp = line.split()
            surname, salary, *_ = tmp
            if int(salary) < 20000:
                less_then_20k.append(surname)
            count += 1
            all_salary += int(salary)
except IOError:
    print("Произошла ошибка ввода-вывода!")

if len(less_then_20k):
    print("Сотрудники имеющие оклад менее 20 тыс:")
    print("\n".join(less_then_20k))
else:
    print("Нет сотрудников имеющих оклад менее 20 тыс")

print("Средний оклад:", all_salary/count)