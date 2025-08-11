'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i]
 is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_mult = []
        post_mult = []
        temp = 1
        for i in nums:
            temp = temp * i
            pre_mult.append(temp)
        temp = 1
        for j in range(len(nums) - 1, -1, -1):
            temp = temp * nums[j]
            post_mult.append(temp)
        post_mult.reverse()

        res = []
        n = len(nums)
        for k in range(n):
            pre = pre_mult[k - 1] if k >= 1 else 1
            post = post_mult[k + 1] if k < n-1 else 1
            res.append(pre * post)
        return res


nums = [1, 2, 3, 4]
sol = Solution()
print((sol.productExceptSelf(nums)))
