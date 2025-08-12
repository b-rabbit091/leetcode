'''
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        k = set(nums)
        max_count = 1
        for i in k:
            if i - 1 not in k:
                count = 0
                current_mem = i
                while current_mem in k:
                    current_mem += 1
                    count += 1
                max_count = max(max_count, count)

        return max_count


nums = [100, 4, 200, 1, 3, 2]
sol = Solution()
print(sol.longestConsecutive(nums))
