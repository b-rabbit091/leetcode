'''

209. Minimum Size Subarray Sum
Medium
Topics
premium lock icon
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


'''
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float('inf')
        presum = 0
        left, right = 0, 0
        while right < len(nums):
            presum += nums[right]

            while presum >= target:
                mini = min(mini, right - left + 1)
                presum -= nums[left]
                left += 1

            right += 1

        return mini if mini != float('inf') else 0


target = 4
nums = [1, 4, 4]

sol = Solution()
print(sol.minSubArrayLen(target, nums))

# Test cases for Leetcode 209: Minimum Size Subarray Sum

tests = [
    # Examples
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),

    # Edge cases
    (1, [1], 1),
    (2, [1], 0),
    (5, [5], 1),
    (6, [5], 0),

    # Minimal window at start
    (6, [6, 1, 1, 1], 1),
    (7, [7, 1, 1, 1], 1),

    # Minimal window at end
    (7, [1, 1, 1, 1, 7], 1),
    (9, [1, 2, 3, 4, 5], 2),  # [4,5]

    # Whole array needed
    (15, [1, 2, 3, 4, 5], 5),

    # No possible subarray
    (100, [1, 2, 3, 4, 5], 0),

    # Many small numbers
    (8, [1, 1, 1, 1, 1, 1, 1, 1], 8),
    (8, [1, 1, 1, 1, 1, 1, 1, 2], 7),

    # Larger values mixed
    (10, [2, 5, 3, 2, 8], 2),  # [2,8]
    (8, [2, 3, 1, 2, 4, 3], 3),  # [2,4,3]

    # Repeated big values
    (9, [9, 9, 9], 1),
    (18, [9, 9, 9], 2),
    (27, [9, 9, 9], 3),
    (28, [9, 9, 9], 0),

    # Stress-style pattern (still small)
    (50, [10, 1, 1, 1, 10, 10, 1, 1, 10, 5], 5),
]

# Assumes your solution is named Solution and method is minSubArrayLen
sol = Solution()

for i, (target, nums, expected) in enumerate(tests, 1):
    result = sol.minSubArrayLen(target, nums)
    print(f"Test {i}: target={target}, nums={nums}")
    print("Expected:", expected)
    print("Got     :", result)
    print("Correct :", result == expected)
    print("-" * 50)
