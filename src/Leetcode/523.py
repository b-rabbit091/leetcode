'''
523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

'''


from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        res = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            res.append(curr_sum % k)
        mp = {0: -1}
        for idx, val in enumerate(res):
            if val not in mp:
                mp[val] = idx
            else:
                diff = idx - mp[val]
                if diff >= 2:
                    return True
        return False
