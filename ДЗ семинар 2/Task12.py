# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а 
# Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

import math

s = int(input('Введите первое число от 0 до 1000: '))
p = int(input('Введите второе число от 0 до 1000: '))

# Решаем систему уравнений s=x+y, p=x*y

x = int((s - math.sqrt(s**2-4*p)) // 2)
y = int((s + math.sqrt(s**2-4*p)) // 2)

print(x, y)


# Второе решение через массив

arr = []
for i in range(s + p):
    if i == (s * i - p)**0.5:
        arr.append(i)
print(*arr if len(arr) == 2 else arr + arr)


# Было в примере (ГЕНИАЛЬНО ПРОСТО)

for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)