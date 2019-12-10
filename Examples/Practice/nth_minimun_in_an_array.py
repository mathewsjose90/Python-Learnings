
def nth_min(arr, n):
    '''
    Checking where the 1st element in the array has to be placed , such that
    all elements to the left of this position will be less than ,and all elements to
    the right will be greater than the number .
    Then will ne repeating the logic with one side of the array from that position
    based on the value of n
    :param arr:
    :param n:
    :return:
    '''
    #print("Called with " + str(arr) + str(n))
    min = arr[0]
    min_pos = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            new_min = arr[i]
            for j in range(i, min_pos, -1):
                arr[j] = arr[j - 1]
            arr[min_pos + 1] = min
            arr[min_pos] = new_min
            min_pos += 1
    if min_pos + 1 == n:
        return min
    elif min_pos + 1 < n:
        return nth_min(arr[min_pos + 1:], n - (min_pos + 1))
    else:
        return nth_min(arr[:min_pos], n)


arr = [12, 33, 4, 6, 5, 2, 7, 9]
for i in range(len(arr)):
    print("{0}th smallest is {1} ".format(i+1, nth_min(arr, i+1)))
