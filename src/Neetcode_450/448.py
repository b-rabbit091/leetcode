'''

448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]



[1,2,2,3,3,4,7,8]
'''

from collections import deque
from typing import List


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        length = len(nums)
        nums = set(nums)
        res = []
        for i in range(1, length+1):
            if i not in nums:
                res.append(i)
        return res



sol = Solution()
nums = [1, 1, 1]
print(sol.findDisappearedNumbers(nums))
