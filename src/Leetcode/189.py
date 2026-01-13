'''

189. Rotate Array
Medium
Topics
premium lock icon

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        left = 0
        idx = 0
        bk = nums.copy()
        while idx < len(nums):
            new_indx = (left + k) % len(nums)
            nums[new_indx] = bk[left]
            left += 1
            idx += 1


nums = [-1, -100, 3, 99]
k = 0
sol = Solution()
sol.rotate(nums, k)
