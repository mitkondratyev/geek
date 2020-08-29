def my_func():
    summ = 0
    spec_symbol = "!"
    finish_func = False
    print("Для выхода из программы введите ", spec_symbol)
    while True:
        tmp = input("Введите числа через пробел:")
        tmp = tmp.split()
        for num in tmp:
            if num == spec_symbol:
                finish_func = True
                break
            summ = summ + int(num)
        print("Сумма = ", summ)
        if finish_func:
            break



my_func()