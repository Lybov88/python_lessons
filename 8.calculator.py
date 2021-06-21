#  *** Калькулятор ***

# функция-обработчик
def calculate(n1, n2, op):
    if op == '+':
        res = n1 + n2
    elif op == '-':
        res = n1 - n2
    elif op == '*':
        res = n1 * n2
    elif op == '/':
        res = n1 / n2
    else:
        res = f"Что это такое: {op}? :("
    return res


#  цикл программы
while True:
    #  ввод данных
    cmd = input("Введите команду ")
    if cmd == "stop":
        print("Bye, bye")
        break

    num_1 = int(input("Введите 1 число: "))
    num_2 = int(input("Введите 2 число: "))
    op = input("Введите символ операции: ")

    # обработка данных
    res = calculate(num_1, num_2, op)

    # вывод данных
    print(f"Результат: {res}")
