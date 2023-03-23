# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


s = ("a a a b c a a d c d d").split()
dict = {}
for i in s:
    if i not in dict:
        dict[i] = 0
        print(i, end=' ')
    elif i in dict:
        dict[i] += 1
        print(f'{i}_{dict[i]}', end=' ')

        

# my_input = input('Введите строку--> ').split()
# my_result = []
# my_dict = dict()
# for i in my_input:
#     my_result.append(i)
#     if i in my_dict:
#         my_result.append('_' + str(my_dict[i]))
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1
# print(*my_result)



# list = 'a a a b c a a d c d d'
# list = list.replace(' ','')
# #list = str.split(' ')
# print(list)
# i, n,str =0, len(list),''

# while i<n:
#     if list[:i].count(list[i])==0 : str += f'{list[i]} '
#     else : str += f'{list[i]}_{list[:i].count(list[i])} '
#     i +=1
# print(str)