# Существует два основных способа реализации алгоритма сортировки слиянием, 
# один из которых использует подход сверху вниз, и именно так чаще всего используется. (Нисходящий)

# Основная идея алгоритма состоит в том, чтобы разделить (под) массивы пополам и отсортировать их рекурсивно. 
# Мы будем продолжать делать это как можно больше, то есть до тех пор, пока не получим подмассивы, 
# которые имеют только один элемент.

# Merge Sort – эффективный алгоритм сортировки общего назначения. 
# Его основным преимуществом является надежное время выполнения алгоритма и 
# его эффективность при сортировке больших массивов. В отличие от быстрой сортировки, 
# он не зависит от каких-либо неудачных решений, которые приводят к плохому времени выполнения.

# Одним из основных недостатков является дополнительная память, 
# которую сортировка слиянием использует для хранения временных копий массивов перед их объединением. 
# Тем не менее, Merge Sort является отличным, интуитивно понятным примером для ознакомления будущих
# инженеров-программистов с подходом «разделяй и властвуй».

def merge_sort(nums):
    if len(nums) > 1:
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

    merge_sort(left)
    merge_sort(right)
    i = j = k = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1

        else:
            nums[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)

# второй вариант не работает

# import operator  #что это не знаю
# def merge_sort(L, compare=operator.lt): # что это не знаю
#     if len(L) < 2:
#         return L[:]
#     else:
#         middle = int(len(L) / 2)
#         left = merge_sort(L[:middle], compare)
#         right = merge_sort(L[middle:], compare)
#         return merge(left, right, compare) # Последним вызовом метода merge мы гарантируем, 
#     # что все деления произойдут до того, как мы начнем сортировку.
    
# def merge(left, right, compare):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if compare(left[i], right[j]):
#             result.append(left[i])
#             i += 1            
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# array = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
# merge_sort(array)