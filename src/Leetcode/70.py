'''

70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''


class Solution:

    def solve(self, n, csum, mp, ind):
        count = 0

        if csum in mp:
            return mp[csum]
        if csum == n:
            return count + 1
        else:
            for i in [1, 2]:
                if csum + i <= n:
                    count += self.solve(n, csum + i, mp, ind + 1)

        mp[csum] = count
        return count

    def climbStairs(self, n: int) -> int:
        csum = 0
        mp = dict()
        ind = 0
        return self.solve(n, csum, mp, ind)


sol = Solution()
n = 7
print(sol.climbStairs(n))
