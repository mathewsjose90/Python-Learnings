'''
rotate a matrix of dimension n*n 90 degreees
ex:
[[1,2,3],     [[7,4,1],
[4,5,6],   ==>[8,5,2],
[7,8,9]       [9,6,3]]
]
'''

arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

## Below solution will take extra space as it is using an extra array for storing the result
result_arr = [[] for _ in range(len(arr))]
for curr_arr in reversed(arr):
    for pos, i in enumerate(curr_arr):
        result_arr[pos].append(i)

print(result_arr)

## Now try without using extra space

# first transpose the matrix
n = len(arr)
for i in range(n):
    for j in range(i, n):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# now for each row swap the element with the symmetrical element from the right
for i in range(n):
    for j in range(n // 2):
        arr[i][j], arr[i][n - 1 - j] = arr[i][n - 1 - j], arr[i][j]

print(arr)
