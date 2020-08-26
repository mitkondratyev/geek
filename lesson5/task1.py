while True:
    tmp = input('Введите строку:')
    if tmp == "":
        break
    f_obj = open("task1.txt", 'a')
    f_obj.write(tmp+"\n")
    f_obj.close()