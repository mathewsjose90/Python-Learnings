'''
Given an array check that if it can be partitioned into 2 arrays , such that the sum of
both the arrays are equal.Re ordering is allowed
Ex:
[1,3,5,3]==>[1,5] and [3,3]  ==>True
[6,7,1,12]==> False
'''

from collections import defaultdict


class Solution:
    @staticmethod
    def partition_possibility(arr):
        result = defaultdict(set)
        result[0].add(0)
        # Consider the elements of array starting as 1 . Then try adding each elements
        # to the left subset or right subset.
        # combination_value=sum of left sub set - sum of right sub set
        # Once we reach the last element we need to see
        # if there was any combination that made the combination_value as 0
        # If 0 is available then there was possibility to split
        for pos, item in enumerate(arr):
            current_pos = pos + 1
            for sum_combination in result[current_pos - 1]:
                result[current_pos].add(sum_combination + item)
                result[current_pos].add(sum_combination - item)

        return 0 in result[len(arr)]

    @staticmethod
    def find_partition(arr, n, pos, left_arr, right_arr):
        # print("called with "+str((arr, n, pos, left_arr, right_arr)))
        if n == pos:
            if sum(left_arr) == sum(right_arr):
                print(left_arr)
                print(right_arr)
                return True
            else:
                return False
        left_arr.append(arr[pos])
        res = Solution.find_partition(arr, n, pos + 1, left_arr.copy(), right_arr.copy())
        if res:
            return True
        else:
            left_arr.pop()
            right_arr.append(arr[pos])
            res = Solution.find_partition(arr, n, pos + 1, left_arr.copy(), right_arr.copy())
            return res


data = [4, 1, 3, 2, 1, 11, 10]
print(Solution.find_partition(data, len(data), 0, [], []))
