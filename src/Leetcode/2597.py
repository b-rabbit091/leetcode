'''

2597. The Number of Beautiful Subsets

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums.
Two subsets are different if and only if the chosen indices to delete are different.



Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

'''

from typing import List


class Solution:

    def solve(self, ind, cdiff, res, mp_ind, nums, k):
        if len(mp_ind)>0:
            res += 1
        for i in range(ind, len(nums)):
            if i in mp_ind.keys() or (nums[i]-k or nums[i]+k) in mp_ind.values():
                continue
            mp_ind[i] = nums[i]
            res = self.solve(i + 1, cdiff, res, mp_ind, nums, k)
            del mp_ind[i]
        return res
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ind = 0
        cdiff = 0
        nums.sort()
        res = 0
        mp_ind = dict()
        res = self.solve(ind, cdiff, res, mp_ind, nums, k)
        return res
sol = Solution()
nums = [1, 2, 4, 5, 7, 10]
k = 3
print(sol.beautifulSubsets(nums, k))

tests = [
    # example 1
    ([2, 4, 6], 2, 4),

    # example 2
    ([1], 1, 1),

    # no pair has difference k
    ([1, 3, 5], 10, 7),

    # all pairs conflict with k = 1
    ([1, 2, 3], 1, 4),

    # duplicates
    ([1, 1, 2], 1, 3),

    # duplicates with no conflict
    ([2, 2, 2], 1, 7),

    # mixed case
    ([4, 2, 5, 9, 10, 3], 1, 23),

    # conflict chain
    ([1, 3, 5, 7], 2, 7),

    # larger k
    ([10, 4, 5, 7, 2, 1], 3, 23),

    # repeated conflict values
    ([1, 1, 3, 3], 2, 8),
]

sol = Solution()

for nums, k, expected in tests:
    result = sol.beautifulSubsets(nums, k)
    print(nums, k, "=>", result, "expected:", expected)
