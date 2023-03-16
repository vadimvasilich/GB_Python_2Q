# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2

from random import randint

n = int(input('Введите количество монет: '))

digit = eagle = 0
coins_list = []
for i in range(n):
    coins_list.append(randint(0,1))
    
print(coins_list)

for i in coins_list:

    if i == 1:
        digit += 1
    
    else:
        eagle += 1

print(eagle if eagle <= digit else digit)

# n = int(input('Введите количество монет '))
# digit = eagle = 0

# for i in range(n):
#     x = int(input('Орел(1) или решка(0)? '))
#     if x == 1:
#         eagle += 1
#     else:
#         digit += 1

# print(eagle if eagle <= digit else digit)
