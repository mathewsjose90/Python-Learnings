def partiton(arr, l, h):
    i = l
    j = h
    while i < j:
        current_element = arr[i]
        while i <= j and arr[i] <= current_element:
            i += 1
        while j >= i and arr[j] > current_element:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[l] = arr[l], arr[j]
    return j


def quicksort(arr, l, h):
    if l < h:
        partition_pos = partiton(arr, l, h)
        quicksort(arr, l, partition_pos)
        quicksort(arr, partition_pos + 1, h)


arr = [2, 4, 67, 33, 45, 10, 41, 6]
quicksort(arr, 0, len(arr) - 1)
print(arr)
