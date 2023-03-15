# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, 
# выведите число -1.

# Input:     5
# Output:  6

number = int(input("Введите число: "))
f1 = f2 = 1
n=3 # число больше 1
while number>f2 :
    f1, f2 = f2, f1 + f2
    n +=1
print(n if number == f2 else '-1')


# a = int(input("Введите число А: "))
# fib_1 = 0
# fib_2 = 1
# i = 2
# index = -1
# while fib_2 < a:
#     fib_sum = fib_1 + fib_2
#     fib_1 = fib_2
#     fib_2 = fib_sum
#     i += 1
#     if a == fib_sum:
#         index = i
# print(index)


# digit = int(input("Enter digit :   "))
# a, b = 1, 1
# flag = True
# count = 0

# while flag:
#     a, b = b, a + b
#     count += 1
#     if digit == a:
#         print(f"digit {digit} fibo!!! position: {count + 2}")
#         flag = False
#     elif a > digit:
#         print(f"sorry, digit {digit} not fibo :(")
#         flag = False


# a=int(input("введите а "))
# first=0
# second=1

# if a==0:
#     print(1)
# elif a==1:
#     print(2)

# count=2
# while second<a:
#     buffer=first+second
#     first=second
#     second=buffer
#     count+=1
# if second==a:
#     print(count)
# else:
#     print(-1)