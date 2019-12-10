'''
MINIMUM STEPS TO ONE
http://www.spoj.com/problems/MST1/
On a positive integer, you can perform any one of the following 3 steps.
1. Subtract 1 from it.
2. If its divisible by 2, divide by 2.
3. If its divisible by 3, divide by 3. Now the question is, given a positive integer n, find the minimum
number of steps that takes n to 1.
'''
import math


def min_steps_to_1_recursive(n):
    if n == 1:
        return 0
    if n % 2 == 0 and n % 3 == 0:
        return min(1 + min_steps_to_1_recursive(n - 1), 1 + min_steps_to_1_recursive(n / 2),
                   1 + min_steps_to_1_recursive(n / 3))
    elif n % 2 == 0:
        return min(1 + min_steps_to_1_recursive(n - 1), 1 + min_steps_to_1_recursive(n / 2))
    elif n % 3 == 0:
        return min(1 + min_steps_to_1_recursive(n - 1), 1 + min_steps_to_1_recursive(n / 3))
    else:
        return 1 + min_steps_to_1_recursive(n - 1)


def min_steps_to_1_dp(n):
    global dp
    if n <= 1:
        return 0
    if dp[n] != 0:
        return dp[n]
    for i in range(2, n + 1):
        dp[i] = 1 + min_steps_to_1_dp(i - 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + min_steps_to_1_dp(i // 2))
        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + min_steps_to_1_dp(i // 3))
    return dp[n]


n = int(input("Enter the number : "))
print(min_steps_to_1_recursive(n))
dp = [0, 0]
for i in range(2, n + 1):
    dp.append(0)
print(min_steps_to_1_dp(n))
