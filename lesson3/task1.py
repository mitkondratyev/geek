def divide(a, b):
    val = 0
    try:
        val = a/b
    except ZeroDivisionError:
        print("Нельзя делить на ноль")
    except Exception:
        print("Ошибка в переменных")
    return val

print(divide(1, "2"))
print(divide(1, 2))
print(divide(1, 0))