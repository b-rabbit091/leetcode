'''
1658. Minimum Operations to Reduce X to Zero

You are given an integer array nums and an integer x.
In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x.
Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
'''

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        element_sum = total_sum - x
        left = 0
        right = 0
        curr_sum = 0
        maxi = -1

        while right < len(nums):
            curr_sum += nums[right]
            while left < len(nums) and (curr_sum > element_sum):
                curr_sum -= nums[left]
                left += 1
            if curr_sum == element_sum:
                maxi = max(maxi, right - left + 1)
            right += 1

        return -1 if maxi == -1 else len(nums) - maxi


sol = Solution()
# nums = [1, 1, 4, 2, 3]
# x = 5
# print(sol.minOperations(nums, x))
# Test cases for Leetcode 1658: Minimum Operations to Reduce X to Zero

tests = [
    # Examples
    ([1, 1, 4, 2, 3], 5, 2),
    ([5, 6, 7, 8, 9], 4, -1),
    ([3, 2, 20, 1, 1, 3], 10, 5),

    # Edge cases
    ([1], 1, 1),
    ([1], 2, -1),
    ([10], 10, 1),
    ([10], 0, 0),

    # x == sum(nums) => remove all
    ([1, 2, 3], 6, 3),
    ([5, 5, 5], 15, 3),

    # x == 0 => 0 operations
    ([1, 2, 3], 0, 0),
    ([100, 1, 1], 0, 0),

    # Remove from left only
    ([1, 2, 3, 4], 6, 3),  # remove 1+2+3
    ([2, 2, 2, 2], 4, 2),

    # Remove from right only
    ([1, 2, 3, 4], 7, 2),  # remove 3+4
    ([1, 1, 1, 1], 2, 2),

    # Mixed ends best
    ([1, 1, 1, 2, 3, 4], 5, 2),  # remove 1 (left) + 4 (right)
    ([4, 1, 1, 1, 2, 3], 7, 3),  # remove 4 (left) + 3 (right) OR other

    # Not possible (x too big)
    ([1, 2, 3], 10, -1),

    # Multiple solutions, choose min ops
    ([5, 1, 1, 1, 1, 1, 5], 10, 2),  # remove both 5s
    ([1, 2, 3, 4, 5], 5, 1),  # remove 5 (right) OR 1+4? min is 1

    # Duplicates / long window keep
    ([1, 1, 1, 1, 1, 1], 3, 3),
    ([3, 1, 1, 1, 1, 1, 1, 3], 6, 2),  # remove 3+3

    # Stress-style small
    ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15, 2),
    # remove 7+8? (right) no; best is 6+9? not ends; actual best: remove 10(left)+5(right)=2
]

sol = Solution()

for i, (nums, x, expected) in enumerate(tests, 1):
    result = sol.minOperations(nums, x)
    print(f"Test {i}: nums={nums}, x={x}")
    print("Expected:", expected)
    print("Got     :", result)
    print("Correct :", result == expected)
    print("-" * 60)
