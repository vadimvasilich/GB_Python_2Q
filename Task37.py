# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы 
# (даже для ввода и вывода).

# Input:  2 -> 3 4
# Output: 4 3

def rev_str(n):
    el = input()
    if n == 1:
        return el
    return rev_str(n - 1) + ' ' + el

n = int(input())
print(rev_str(n))


# def num_reverse(m):
#     if m == 0:
#         return
#     x = input()
#     num_reverse(m - 1)
#     print(x)

# n = int(input('N = '))
# num_reverse(n)