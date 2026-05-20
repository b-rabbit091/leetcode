'''

322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

'''
from typing import List


class Solution:

    def solve(self, res, dp, csum, coins, amount):

        if csum == amount:
            return len(res)

        elif csum > amount:
            return float('inf')

        if csum in dp:
            return dp[csum]

        mini = float('inf')

        for i in range(0, len(coins)):
            if csum + coins[i] <= amount:
                mini = min(mini, 1 + self.solve(res, dp, csum + coins[i], coins, amount))
        dp[csum] = mini
        return dp[csum]

    def coinChange(self, coins: List[int], amount: int) -> int:
        res = []
        dp = {}
        res = self.solve(res, dp, 0, coins, amount)
        return res if type(res) is int else -1


sol = Solution()
coins = [1, 2, 5]
amount = 11
print(sol.coinChange(coins, amount))

tests = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1], 1, 1),
    ([1], 2, 2),
    ([2, 5, 10, 1], 27, 4),
    ([186, 419, 83, 408], 6249, 20),
    ([3, 7, 405, 436], 8839, 25),
    ([5], 10, 2),
    ([5], 3, -1),
    ([2, 4], 7, -1),
    ([1, 3, 4], 6, 2),
]

sol = Solution()
correct = 0

for coins, amount, expected in tests:
    result = sol.coinChange(coins, amount)

    if result == expected:
        correct += 1

    print(coins, amount, "=>", result, "expected:", expected)

print("Correct:", correct, "/", len(tests))
