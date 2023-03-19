# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n,k=len(list),3

while k>0 :
    list.append(list[0])
    list.pop(0)
    k -=1
print (list)


#2
# list_1 = [1, 2, 3, 4, 5]
# k = 6 % len(list_1)

# for i in range(k):
#     num = list_1.pop(-1)
#     list_1.insert(0, num)
# print(list_1)


#3
# n = [1, 2, 3, 4, 5]
# k = 5 % len(n)
# new_list = n[k:] + n[:k] 
# print(new_list)