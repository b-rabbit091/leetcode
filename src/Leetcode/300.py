'''
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''
from typing import List


class Solution:
    def solve(self, ind, nums, dp):

        if dp.get(ind, -1) != -1:
            return dp[ind]

        if ind >= len(nums):
            return 1
        prev_count = 1
        for i in range(ind, len(nums)):
            if nums[ind] < nums[i]:
                count = 1 + self.solve(i, nums, dp)
                prev_count = max(count, prev_count)
        dp[ind] = prev_count
        return prev_count

    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        dp = {}
        for i in range(0, len(nums)):
            ans = max(ans, self.solve(i, nums, dp))
        return ans

test_cases = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),

    ([], 0),
    ([1], 1),
    ([1, 2], 2),
    ([2, 1], 1),

    ([1, 2, 3, 4, 5], 5),
    ([5, 4, 3, 2, 1], 1),
    ([2, 2, 2, 2], 1),

    ([4, 10, 4, 3, 8, 9], 3),
    ([1, 10, 2, 9, 3, 8, 4, 7], 5),
    ([3, 4, -1, 0, 6, 2, 3], 4),
    ([50, 3, 10, 7, 40, 80], 4),
    ([1, 101, 2, 3, 100, 4, 5], 5),

    ([-1, -2, -3, -4], 1),
    ([-4, -3, -2, -1], 4),
    ([-1, 3, 4, -2, 0, 6, 2, 3], 4),

    ([1, 1, 2, 2, 3, 3], 3),
    ([2, 1, 3, 2, 4, 3, 5], 4),
    ([5, 1, 5, 2, 5, 3, 5, 4], 5),
]

sol = Solution()

correct = 0
false = 0

for nums, expected in test_cases:
    output = sol.lengthOfLIS(nums)

    if output == expected:
        correct += 1
        status = "Correct"
    else:
        false += 1
        status = "False"

    print(nums, "=> output:", output, "expected:", expected, status)

print("Correct:", correct)
print("False:", false)
