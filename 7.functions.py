#  *** Функции ***

# встроенная функция ввода данных
# data = input("Введите данные: ")

# print(f"Вы ввели вот это - {data}")

# Создание (определение) функции

# 1 вариант. Функция, принимающая данные (обладающая аргументами)


def func_1(arg_1):
    s = arg_1 ** 2
    w = s + 10
    print(f"результат: {w}")


# вызов функции
# func_1(1000)

def func_2(a, b, c):
    res = a + b + c
    res += 200
    print(res)

# func_2(10, 5, 2)

# функция с аргументом. аргумент может иметь значение по умолчанию


def func_3(arg_1, arg_2=100):
    print(arg_1 * arg_2)


func_3(20, 10)