def lcs(arr1, arr2, i, j):
    if i >= len(arr1) or j >= len(arr2):
        return 0
    if arr1[i] == arr2[j]:
        return 1 + lcs(arr1, arr2, i + 1, j + 1)
    return max(lcs(arr1, arr2, i + 1, j), lcs(arr1, arr2, i, j + 1))


string1 = "abcdefzbr"
string2 = "acdhfxgbn"

print(lcs(string1, string2, 0, 0))

# Solution 2 is below
# We are constructing a 2 dimensional array with the  order (m*n)
# And 1 additional row and column to initialize the value 0*0 in 1st row and colum

result_arr = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        if string1[i - 1] == string2[j - 1]:
            # If ith anf jth positions match then add 1 to the previuos value diagonally in the matrix
            result_arr[i][j] = result_arr[i - 1][j - 1] + 1
        else:
            result_arr[i][j] = max(result_arr[i - 1][j], result_arr[i][j - 1])

print("Length of longest common subsequence is : "+str(max([max(i) for i in result_arr])))
print(result_arr)
# BackTrack for the longest string from the result array
i = len(string1)
j = len(string2)
result_str = ""

while (i > 0 and j > 0):
    if result_arr[i - 1][j - 1] != result_arr[i][j]:
        if result_arr[i][j] != result_arr[i][j - 1] and result_arr[i][j] != result_arr[i - 1][j]:
            result_str = string1[i - 1] + result_str
            i -= 1
            j -= 1
        if result_arr[i][j] in (result_arr[i][j - 1], result_arr[i - 1][j]):
            if result_arr[i][j] == result_arr[i][j - 1]:
                j -= 1
            else:
                i -= 1
    else:
        i -= 1
        j -= 1

print(result_str)
