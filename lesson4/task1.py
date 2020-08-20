from sys import argv

def salary(hours, rate, bonus):
    return (hours * rate) + bonus

help_text = """Формат использования программ
                \t task1.py hours rate bonus
                \t hours - выработка в часах
                \t rate - ставка в час
                \t bonus - премия"""

if len(argv) != 4:
    print("Ошибка в количестве параметров")
    print(help_text)
    exit(0)

_, *args = argv

input_error = False
for idx, itm in enumerate(args):
    try:
        args[idx] = float(itm)
    except ValueError:
        print("Ошибка ввода")
        input_error = True
        break

if input_error:
    exit(0)

print(salary(*args))