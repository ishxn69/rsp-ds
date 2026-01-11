arr = [2, 3, 4, 7, 8, 12, 16, 18]

def binary_search(nums, left, right, target):
    # right >= left
    if right >= left: 
        # calculate the mid point
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # mid is greater than target
        elif nums[mid] > target:
            return binary_search(nums, left, mid - 1, target)
        
        # mid is less than target
        else:
            return binary_search(nums, mid + 1, right, target)
    # element is not in the array
    else:
        return -1

print(binary_search(arr, 0, len(arr) - 1, 9))
