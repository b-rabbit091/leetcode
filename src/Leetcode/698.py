'''



698. Partition to K Equal Sum Subsets
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


'''
import math
from typing import List


class Solution:

    def solve(self, mp_ind, csum, ind, target, nums,k):
        if k==0:
            return True

        if csum == target:
            return self.solve(mp_ind, 0, 0, target, nums, k - 1)

        for i in range(ind, len(nums)):
            if i in mp_ind or csum + nums[i] > target:
                continue
            mp_ind.add(i)
            if self.solve(mp_ind, csum + nums[i], i + 1, target, nums, k):
                return True
            mp_ind.remove(i)
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        mp_ind = set()
        csum = 0
        ind = 0
        target = sum(nums) / k
        res = self.solve(mp_ind, csum, ind, target, nums, k)
        return res


sol = Solution()
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
sol.canPartitionKSubsets(nums, k)
tests = [
    # example true
    ([4, 3, 2, 3, 5, 2, 1], 4, True),

    # example false
    ([1, 2, 3, 4], 3, False),

    # cannot divide total sum equally
    ([1, 2, 3, 5], 2, False),

    # each number is its own subset
    ([1, 1, 1, 1], 4, True),

    # k = 1, always true
    ([2, 3, 5, 7], 1, True),

    # one element bigger than target
    ([10, 1, 1, 1, 1], 2, False),

    # duplicate numbers
    ([2, 2, 2, 2, 3, 4, 5], 4, False),

    # possible with equal pairs
    ([2, 2, 2, 2, 2, 2], 3, True),

    # possible with mixed numbers
    ([1, 1, 2, 2, 2], 2, True),

    # harder true case
    ([6, 5, 4, 3, 2, 1], 3, True),

    # harder false case
    ([3, 3, 3, 3, 4], 4, False),
]

sol = Solution()

for nums, k, expected in tests:
    result = sol.canPartitionKSubsets(nums, k)
    print(nums, k, "=>", result, "expected:", expected)