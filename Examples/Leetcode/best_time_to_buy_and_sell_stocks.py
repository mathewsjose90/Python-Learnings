'''
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
'''


class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            one_day_profit = prices[i] - prices[i - 1]
            profit += max(0, one_day_profit)
        return profit
