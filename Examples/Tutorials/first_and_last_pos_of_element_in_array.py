def searchRange(nums, target):
    def get_first_pos_ge_x(arr, x):
        low = 0
        high = len(arr) - 1
        first_pos = len(arr)  # initilaize after the end of array for no match
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:  # If there is a number greater than x then check on the left part
                first_pos = mid
                high = mid - 1
            else:
                low = mid + 1  # else check on the right part of mid
        return first_pos

    start_location = get_first_pos_ge_x(nums, target)
    end_location = get_first_pos_ge_x(nums, target + 1) - 1
    print(start_location,end_location)
    if start_location <= end_location:
        return [start_location, end_location]
    else:
        return [-1, -1]


arr = [5, 7, 7, 8, 8, 10]
arr1 = [1, 9, 10]
target = 8
print(searchRange(arr, target))
