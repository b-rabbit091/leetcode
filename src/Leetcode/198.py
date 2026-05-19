'''
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have security
 systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

'''
from typing import List


class Solution:

    def solve(self, mp, ind, nums, res):

        if mp.get(ind, -1) != -1:
            return mp.get(ind)

        if ind >= len(nums):
            return 0
        rob_house = nums[ind] + self.solve(mp, ind + 2, nums, res)
        skip_house = self.solve(mp, ind + 1, nums, res)

        mp[ind] = int(max(rob_house, skip_house))
        return mp[ind]

    def rob(self, nums: List[int]) -> int:
        mp = {}
        ind = 0
        res = 0
        res = self.solve(mp, ind, nums, res)
        return res


nums = [2, 7, 9, 3, 1]
sol = Solution()
print(sol.rob(nums))

tests = [
    # example 1
    ([1, 2, 3, 1], 4),

    # example 2
    ([2, 7, 9, 3, 1], 12),

    # single house
    ([5], 5),

    # two houses
    ([2, 1], 2),

    # all same
    ([4, 4, 4, 4], 8),

    # alternating large values
    ([10, 1, 10, 1, 10], 30),

    # increasing values
    ([1, 2, 3, 4, 5], 9),

    # decreasing values
    ([9, 8, 7, 6, 5], 21),

    # zeros
    ([0, 0, 0], 0),

    # tricky case
    ([2, 1, 1, 2], 4),

    # larger mixed
    ([6, 7, 1, 30, 8, 2, 4], 41),

    # another tricky one
    ([5, 1, 1, 5], 10),
]

sol = Solution()

for nums, expected in tests:
    print(nums, "=>", sol.rob(nums), "expected:", expected)