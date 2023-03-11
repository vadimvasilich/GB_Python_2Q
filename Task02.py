# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input('Введите трехзначное число: '))

temp1 = num % 10
temp2 = num // 10
temp3 = temp2 % 10
temp4 = num // 100

sum = temp1 + temp3+ temp4
print(f'Сумма цифр равна: {sum}')