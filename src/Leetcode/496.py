'''
496. Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next
greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

'''

from collections import deque
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = {}
        res = deque()
        length = len(nums2) - 1
        for idx in range(length, -1, -1):
            elem = nums2[idx]
            while len(res) > 0 and res[- 1] < elem:
                res.pop()
            default = -1 if len(res) == 0 else res[- 1]
            st[elem] = default
            res.append(elem)
        return [st[val] for val in nums1]


sol = Solution()
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(sol.nextGreaterElement(nums1, nums2))
