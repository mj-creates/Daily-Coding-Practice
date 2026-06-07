def selectionSort(array, size):
    for ind in range(size - 1):
        min_ind = ind
        for j in range(ind+1, size):
            if array[j] < array[min_ind]:
                min_ind = j
        array[ind], array[min_ind] = array[min_ind], array[ind]

arr = [-19, 0, 186, -8, 32, 12, -2]
size = len(arr)
selectionSort(arr , size)
print("Sorted array", arr)