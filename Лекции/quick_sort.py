# Алгоритм бинарного поиска, который
# также принадлежит стратегии “разделяй и властвуй”. 


def quicksort(array):

    if len(array) < 2: # делим интервал попалам
        return array
    
    else:
        pivot = array[0] # присваеваем первое значение 
        # используем срезы влево от середины интервала
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))