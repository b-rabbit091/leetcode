'''

283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zro = 0
        nzr = zro + 1

        while zro < len(nums) and nzr < len(nums):

            while zro < len(nums) and nums[zro] != 0:
                zro += 1

            nzr = zro + 1

            while nzr < len(nums) and nums[nzr] == 0:
                nzr += 1

            if zro < len(nums) and len(nums) > nzr > zro:
                nums[zro], nums[nzr] = nums[nzr], nums[zro]
                zro += 1
        print(nums)


sol = Solution()
nums = [0, 1]
sol.moveZeroes(nums)
