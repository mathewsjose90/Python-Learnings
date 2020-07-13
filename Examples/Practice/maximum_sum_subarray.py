'''
[1,-2,3,2,-4] ==>Find maximum sum sub array . Sub array means continuous elements
maximum sum subarray is [3,2]
'''

#a = [-3, -2, 3, 2, -1, -10, 100]
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = 0
max_sum_so_far = 0
start_index = 0
end_index = 0

for pos, i in enumerate(a):
    if current_sum + i > 0:
        current_sum = current_sum + i
    else:
        current_sum = 0
        start_index = end_index = min(pos + 1, len(a))
    if current_sum > max_sum_so_far:
        end_index = pos

    max_sum_so_far = max(current_sum, max_sum_so_far)

print("Input array is : ", a)
print("Maximum sum for a sub array is : ", max_sum_so_far)
print("Maximum sum sub array is : ", str(a[start_index:end_index + 1]))
