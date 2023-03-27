# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# 2 2
# 4


def sum_number(num1, num2):

    if num2 == 0:
        return num1 
    else:
        return 1 + sum_number(num1, num2 - 1)
    
a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
if a > 0 and b > 0:
    print(sum_number(a, b))
else: print('Ошибка ввода!')