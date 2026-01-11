def binary_search(nums, target):
        # set pointers.
        left = 0 
        right = len(nums) - 1
        # compulsory condition
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # discard the greater half.
            elif target < nums[mid]:
                right = mid - 1
            # discard the smaller half.
            else:
                left = mid + 1
        # we haven't found the element.
        return -1
