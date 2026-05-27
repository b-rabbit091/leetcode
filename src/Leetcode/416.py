'''

416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

'''

from typing import List


class Solution:
    def solve(self, ind, nums, dp, csum, tsum):

        if dp.get((ind, csum), -1) != -1:
            return dp[(ind, csum)]

        if csum == tsum:
            dp[(ind, csum)] = True
            return dp[(ind, csum)]

        elif ind >= len(nums):
            dp[(ind, csum)] = False
            return dp[(ind, csum)]

        sum1 = self.solve(ind + 1, nums, dp, csum + nums[ind], tsum)
        sum2 = self.solve(ind + 1, nums, dp, csum, tsum)

        dp[(ind, csum)] = sum1 or sum2
        return dp[(ind, csum)]

    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        sm = sum(nums)
        if sm % 2 != 0:
            return False
        tsum = sm / 2
        res = self.solve(0, nums, dp, 0, tsum)
        return res


test_cases = [
    ([11, 5, 1, 5], True),
    ([1, 2, 3, 5], False),

    # Edge cases
    ([], True),
    ([1], False),
    ([0], True),
    ([0, 0], True),
    ([0, 0, 0], True),

    # Small cases
    ([1, 1], True),
    ([1, 2], False),
    ([2, 2], True),
    ([2, 3], False),

    # Odd total sum
    ([1, 2, 4], False),
    ([2, 2, 3], False),
    ([100, 1, 2], False),

    # Even total but impossible
    ([2, 2, 2, 3, 5], True),
    ([1, 2, 5], False),
    ([3, 3, 3, 4, 5], True),

    # Duplicates
    ([1, 1, 1, 1], True),
    ([2, 2, 2, 2, 2], False),
    ([4, 4, 4, 4], True),

    # Larger numbers
    ([100, 100], True),
    ([100, 50, 50], True),
    ([100, 99, 1], True),
    ([100, 99, 2], False),

    # Tricky cases
    ([2, 5, 6, 7], False),
    ([1, 3, 5, 9], True),
    ([1, 3, 4, 4], False),
    ([1, 2, 3, 4, 6], True),
    ([1, 2, 3, 9], False),
]
sol = Solution()

correct = 0
wrong = 0

for nums, expected in test_cases:
    output = sol.canPartition(nums)

    if output == expected:
        correct += 1
    else:
        wrong += 1
        print("Wrong:", nums, "output:", output, "expected:", expected)

print("Correct:", correct)
print("Wrong:", wrong)
