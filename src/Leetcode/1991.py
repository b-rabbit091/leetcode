'''

1991. Find the Middle Index in Array

Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

'''
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = 0

        l_map = {}
        r_map = {}
        ln = len(nums)
        for idx in range(ln):
            l_sum += nums[idx]
            r_sum += nums[ln - idx - 1]

            l_map[idx] = l_sum
            r_map[ln - idx - 1] = r_sum

        for keys, value in l_map.items():
            if r_map[keys] == value:
                return keys
        return -1


sol = Solution()
nums = [1, -1, 2, 3, 1, -1]

print(sol.findMiddleIndex(nums))
