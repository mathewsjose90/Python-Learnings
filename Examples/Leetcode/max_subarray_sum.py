'''
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

import sys


class Solution:

    def maxSubArray(self, nums):
        max_sum = -sys.maxsize
        current_sum = 0
        start_pos = end_pos = 0
        for i in range(len(nums)):
            if current_sum + nums[i] > nums[i]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
                start_pos = end_pos = i
            if current_sum > max_sum:
                end_pos = i
            max_sum = max(current_sum, max_sum)
        return max_sum
