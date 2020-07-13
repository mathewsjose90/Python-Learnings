'''
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/
'''


class Solution:

    def isHappy(self, n: int) -> bool:
        def sumofdigitsquares(n):
            sum = 0
            while n:
                digit = n % 10
                n = n // 10
                sum += digit ** 2
            return sum

        visited_numbers = {}
        while True:
            if n == 1:
                return True
            n = sumofdigitsquares(n)
            if n in visited_numbers:
                return False
            visited_numbers[n] = 1
        return False
