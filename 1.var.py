# *** переменные ***
my_var_1 = 100
myVar2 = 200

a = my_var_1 + myVar2

# комментирование ctrl+/
# print(a)

# заглавныеми буквами пишутся названия констант
PI = 3.14

# *** типы данных ***
_int = 100000
_float = 500.001

my_str = "Привет 'мир' !"

# print(my_str)

# булевы типы данных (boolean, bool)
# True / False
my_bool = True  # истина, логическая 1,False - лог 0

#  *** способ форматирования строк под названием "f-строка"
# старейший способ форматирования - конкатенация
z = "Hello"
r = ' '
q = ", World!"

s = z + r + q
# print(s)

res = f"1 слово: {z} 2 слово: {r} 3 строка = {q}"
# print(res)


# ***Арифметические операции***
var_1 = 5
var_2 = 2

# Операция сложения
print(var_1 + var_2)

# Операция вычитания
print(var_1 - var_2)

# Операция умножения
print(var_1 * var_2)

# Операция простого деления
# возвращает всегда тип float
print(var_1 / var_2)

# Операция цлочисленного деления
# всегда тип int и без окргления
print(var_1 // var_2)
