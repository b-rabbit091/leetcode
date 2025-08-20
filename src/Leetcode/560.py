'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

'''
from typing import List


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        st = dict()
        st[0] = 1
        count = 0
        pre_sum = 0
        for num in nums:
            pre_sum += num
            diff = pre_sum - k
            if diff in st.keys():
                count += st[pre_sum]
            st[diff] = st.get(diff, 0) + 1
        return count


nums = [1, 1, 2]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))
