def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and (arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -=1
    return arr
            
arr = [character for character in 'insertionsort']
result = insertion_sort(arr)
print(result)
