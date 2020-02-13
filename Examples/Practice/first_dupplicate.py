'''
Arr elements will be between 1 and length of the array.
Print the first duplicate character .
If no duplicates return -1
'''
import sys

arr = [2, 1, 3, 5, 3, 2]


def find_first_duplicate(arr):
    '''
    Order of n2 it may take
    :param arr:
    :return:
    '''
    start = 0
    min_pos_for_duplicate = sys.maxsize
    arr_length = len(arr)

    while start < arr_length and start < min_pos_for_duplicate:
        # check for duplicate from the next position and if duplicate is available update
        # the duplicate position only if it is less than the current min position for the duplicate.
        duplicate_pointer_pos = start + 1

        while duplicate_pointer_pos < arr_length:
            if arr[duplicate_pointer_pos] == arr[start]:
                if duplicate_pointer_pos < min_pos_for_duplicate:
                    min_pos_for_duplicate = duplicate_pointer_pos
            duplicate_pointer_pos += 1
        start += 1

    if min_pos_for_duplicate == sys.maxsize:
        return (-1)
    else:
        return (arr[min_pos_for_duplicate])


def find_min_pos_with_hash(arr):
    '''
    constant time solution
    :param arr:
    :return:
    '''
    seen = {}
    for item in arr:
        if item not in seen:
            seen[item] = 1
        else:
            return item
    return -1


print(find_first_duplicate(arr))
print(find_min_pos_with_hash(arr))
