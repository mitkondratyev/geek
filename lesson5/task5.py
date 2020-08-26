import random

file_name = "task5.txt"
numbers = [random.randint(0, 10) for _ in range(0, 13)]
#print(numbers)
f_obj = open(file_name, 'w')
f_obj.write(" ".join(str(item) for item in numbers))
f_obj.close()

all_summ = 0
try:
    with open(file_name) as f_obj:
        for line in f_obj:
            nums = [int(n) for n in line.split()]
            all_summ = sum(nums)
except IOError:
    print("Произошла ошибка ввода-вывода!")

print("Сумма:",all_summ)