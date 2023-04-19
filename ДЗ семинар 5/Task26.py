# Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def row_number(num1, num2):
    if num2 == 0:
        return 1  
    else: 
        return num1 * row_number(num1, num2 - 1); 
    
a = int(input('Введите число :'))
b = int(input('Введите степень числа: '))
print(row_number(a, b))