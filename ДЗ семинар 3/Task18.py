# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

number = int(input('Введите количество элементов: '))
our_list = []
for i in range(0, number):
    our_list.append(int(input('Введите элемент: ')))

digit = int(input('Введите число для проверки: '))


# for i in number: #range(len(our_list)):


diff_min = our_list[0]
for j in our_list:
        if abs(j - digit) < abs(diff_min - digit):
              diff_min = j



        
print(diff_min)