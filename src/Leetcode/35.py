'''

Search Insert Position

Given a sorted array of distinct integers and a target value, r
eturn the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        if nums[high] < target:
            return max(0,high + 1)
        return max(0,low - 1)


nums = [1, 3, 5, 6]
target = 2
sol = Solution()
print(sol.searchInsert(nums, target))
