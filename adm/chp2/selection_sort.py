'''Logic: find the minimum in the unsorted array and then put it in place
where it goes in the sorted array'''

def selection_sort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
        
    
arr = [ch for ch in 'selectionsort']
result = selection_sort(arr)
for ch in result: print(ch)
