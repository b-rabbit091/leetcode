'''
347. Top K Frequent Elements

Given an integer array nums and an integer k,
return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
'''

from typing import List


class Solution:


    def TopK(self, arr, mp, low, high):

        if low == high:
            mp[arr[low]] = mp.get(arr[low], 0) + 1
        else:
            mid = (low + high) // 2
            mp = self.TopK(arr, mp, low, mid)
            mp = self.TopK(arr, mp, mid+1, high)

        return mp


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        dct = self.TopK(nums, dct, 0, len(nums) - 1)
        elems = sorted(dct, key=lambda x: dct[x], reverse=True)
        return elems[:k]


sol = Solution()
nums = [1, 2]
k = 2
print(sol.topKFrequent(nums, k))
