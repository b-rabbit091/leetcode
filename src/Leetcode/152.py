'''
152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

from typing import List


class Solution:
    def solve(self, nums):
        maxi = nums[0]
        mini = nums[0]
        res = nums[0]

        for i in nums[1:]:
            temp_maxi = max(maxi * i, mini * i, i)
            temp_mini = min(maxi * i, mini * i, i)

            maxi = temp_maxi
            mini = temp_mini

            res = max(res, maxi)

        return res

    def maxProduct(self, nums: List[int]) -> int:
        return self.solve(nums)


nums = [-1, -2, -3]
sol = Solution()
print(sol.maxProduct(nums))

tests = [
    ([2, 3, -2, 4], 6),
    ([-2], -2),
    ([2, 3, 4], 24),
    ([-2, 3, -4], 24),
    ([-1, -2, -3], 6),
    ([1, -2, -3, 4], 24),
    ([3, -1, 4], 4),
    ([-4, -3, -2], 12),
]

sol = Solution()
correct = 0

for nums, expected in tests:
    result = sol.maxProduct(nums)

    if result == expected:
        correct += 1

    print(nums, "=>", result, "expected:", expected)

print("Correct:", correct, "/", len(tests))
