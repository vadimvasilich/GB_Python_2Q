# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# Input:       5
# Output:    120

# n = int(input('Введите число N: '))
# factorial = 1
# i = 2
# while(i <= n):
#     factorial *= i
#     i += 1
# print(f'N! = {factorial}')

number = int(input('Введите число: '))
factorial = 1
while number > 1:
    factorial *= number 
    number -= 1

print(factorial)