'''

Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.



var_int = 42
var_float = 3.14
var_str = "Hello, world!"
var_list = [1, 2, 3, 4, 5]
var_dict = {'a': 1, 'b': 2, 'c': 3}
var_bool = True
var_none = None

print("Тип переменной var_int:", type(var_int))
print("Тип переменной var_float:", type(var_float))
print("Тип переменной var_str:", type(var_str))
print("Тип переменной var_list:", type(var_list))
print("Тип переменной var_dict:", type(var_dict))
print("Тип переменной var_bool:", type(var_bool))
print("Тип переменной var_none:", type(var_none))


Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты


import sys

data = [42, 3.14, "Hello, world!", [1, 2, 3], {'a': 1, 'b': 2}, True, None]
data.extend([42, "Hello, world!"])

for index, item in enumerate(data, start=1):
    print(f"Порядковый номер: {index}")
    print(f"Значение: {item}")
    print(f"Адрес в памяти: {id(item)}")
    print(f"Размер в памяти: {sys.getsizeof(item)} байт")
    
    if isinstance(item, int) and item > 0:
        print("Результат проверки на целое число: Положительное целое число")
    
    if isinstance(item, str):
        print("Результат проверки на строку: Это строка")
    
    if not isinstance(item, (list, dict)):
        print(f"Хэш объекта: {hash(item)}")
    
    print()



  #  2 вариант


    data = [1, 'shamil', 3.14, True, -1, 'shamil']
for index, value in enumerate(data, 1):
    print(f'порядковый номер: {index}')
    print(f"значение: {value}")
    print(f'адрес в памяти: {id(value)}')
    print((f'размер в памяти: {value.__sizeof__()} байт'))
    print(f'хэш объекта: {hash(value)}')
    if isinstance(value, int):
        print(f'Результат проверки на целое число: True')
    print(f'результат проверки на на строку: ', 'True' if isinstance(value, str) else 'False')
    print('\n', "==" * 40, '\n')



#     ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно


def convert_to_binary_octal(number: int) -> tuple[str, str]:
    binary = ""
    octal = ""
    
    while number > 0:
        binary_digit = str(number % 2)
        binary = binary_digit + binary
        number //= 2
    
    number = number
    while number > 0:
        octal_digit = str(number % 8)
        octal = octal_digit + octal
        number //= 8
    
    return binary, octal

number = int(input("Введите целое число: "))

binary, octal = convert_to_binary_octal(number)

print("Двоичное представление:", binary)
print("Восьмеричное представление:", octal)

###

BIN = 2
OCT = 8
number = 46


def num_to_base(orig_number, base):
    result = ''
    while orig_number != 0:
        result = str(orig_number % base) + result
        orig_number //= base
    return result


print('0b' + num_to_base(number, BIN))
print(bin(number))
print('0o' + num_to_base(number, OCT))
print(oct(number))

# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

pi = 3.141592653589793238462643383279502884197169399375105820974944
diameter = float(input("Введите диаметр круга: "))
if diameter > 1000:
    print("Диаметр не должен превышать 1000 у.е.")
else:
    radius = diameter / 2
    area = pi * radius ** 2
    circum = 2 * pi * radius
    print("Площадь круга:", format(area, '.42f'))
    print("Длина окружности:", format(circum, '.42f'))


# Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

import cmath

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b**2 - 4*a*c

root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

print("Корень 1:", root1)
print("Корень 2:", root2)

###

num = 365

def hex_str(hex_num):
    if hex_num == 0:
        return ''
    result = ''
    while hex_num != 0:
        remainder = hex_num % 16
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
        hex_num //= 16
    return result

hex_representation = hex_str(num)

print("Шестнадцатеричное представление числа:", hex_representation)
print("Проверка результата:", "0x" + hex_representation.lower() if hex_representation else "0x0")

###

'''
frac1 = "1/2"
frac2 = "1/3"

num1, den1 = map(int, frac1.split('/'))
num2, den2 = map(int, frac2.split('/'))

sum_num1 = num1 * den2 + num2 * den1
sum_den1 = den1 * den2

product_num1 = num1 * num2
product_den1 = den1 * den2

sum_result1 = f"{sum_num1}/{sum_den1}"
product_result1 = f"{product_num1}/{product_den1}"

sum_result2 = sum_result1
product_result2 = product_result1

print("Сумма дробей:", sum_result1)
print("Произведение дробей:", product_result1)
print("Сумма дробей:", sum_result2)
print("Произведение дробей:", product_result2)