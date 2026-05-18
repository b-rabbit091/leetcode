'''

746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

'''

from typing import List

class Solution:

    def solve(self, curr_pos, cost, mp):

        if curr_pos >= len(cost):
            return 0

        if mp.get(curr_pos, -1) != -1:
            return mp[curr_pos]

        res = []
        for step in [1, 2]:
            costi = cost[curr_pos]
            res.append(costi + self.solve(curr_pos + step, cost, mp))

        mp[curr_pos] = min(res)
        return mp[curr_pos]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mp = {}
        res = self.solve(0, cost, mp)
        res2 = self.solve(1, cost, mp)
        res = min(res, res2)
        return res


sol = Solution()
cost = [10,15,20,10,10,5,6,7,8,9,20]
print(sol.minCostClimbingStairs(cost))
