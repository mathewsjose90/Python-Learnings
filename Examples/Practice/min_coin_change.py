'''
MINIMUM COIN CHANGE
Given a value N, if we want to make change for N cents, and we have infinite supply of each of
C = { C1, C2, ... , CM} valued coins, what is the minimum number of coins to make the change?
Example :
Input: coins[] = {25, 10, 5}, N = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents
Input: coins[] = {9, 6, 5, 1}, N = 13
Output: Minimum 3 coins required
We can use one coin of 6 + 6 + 1 cents coins.
'''

import sys


def min_coin_change(n, changes):
    if n == 0:
        return 0
    changes_required = sys.maxsize
    for i in range(len(changes)):
        if changes[i] <= n:
            new_changes_required = 1 + min_coin_change(n - changes[i], changes)
            changes_required = min(changes_required, new_changes_required)
    return changes_required


def min_coin_change_dp(n, changes, dp):
    if dp[n] != -1:
        return dp[n]
    if n == 0:
        return 0
    res = sys.maxsize
    for i in range(len(changes)):
        if n >= changes[i]:
            current_res = 1 + min_coin_change_dp(n - changes[i], changes, dp)
            res = min(current_res, res)
    dp[n] = res
    return dp[n]


def main():
    n = int(input("Enter the number :"))
    changes = list(map(int, input("Enter the changes available (Space separated) : ").split()))
    #print(min_coin_change(n, changes))
    dp = [-1] * (n + 1)
    dp[0] = 0
    print(min_coin_change_dp(n, changes, dp))


if __name__ == "__main__":
    main()
