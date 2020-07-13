'''
2 dimensional array of colors given . Find the largest group of colors touching.

[[R,B,B,B,G],
[ R,B,G,G,R], ==> Answer is B , as 5 B's are touching each othre
[ R,B,R,R,G]]

'''

a = [['R', 'B', 'B', 'B', 'G'],
     ['R', 'B', 'B', 'B', 'R'],
     ['R', 'B', 'R', 'R', 'G']]
'''
t = [['R', 'B', 'B', 'B', 'R'],
     ['R', 'B', 'R', 'R', 'R'],
     ['R', 'B', 'R', 'R', 'G']]
'''

row = len(a)
col = len(a[0])
dp = {}


def largest_group(arr, i, j, color, visited_and_counted_pos=[]):
    # print("called with" + str((i, j, color)))
    # Dont calculate already counted position for the same color
    if (i, j) in visited_and_counted_pos:
        return 0
    if (i, j, color) in dp:
        return dp[(i, j, color)]
    if i >= row or i < 0 or j >= col or j < 0:
        return 0
    if arr[i][j] == color:
        visited_and_counted_pos.append((i, j))
        color_count = 1 + largest_group(arr, i, j + 1, color, visited_and_counted_pos) + largest_group(arr, i + 1, j,
                                                                                                       color,
                                                                                                       visited_and_counted_pos)
        # color_count += largest_group(arr, i - 1, j, color) + largest_group(arr, i, j - 1, color)
        dp[(i, j, color)] = color_count
        return color_count
    else:
        dp[(i, j, color)] = 0
        return 0


for row_id, data in enumerate(a):
    for col_id, item in enumerate(data):
        largest_group(a, row_id, col_id, item, [])
        # break

max_occurences = max(dp.values())
print("max occurence is : ", max_occurences)
print("Largest group of colors is : " + str(set([k[2] for k, v in dp.items() if v == max_occurences])))
