'''

219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = dict()
        st = set()
        for ind, val in enumerate(nums):
            if val in st:
                diff = abs(mp[val] - ind)
                if diff <= k:
                    return True
            mp[val] = ind
            st.add(val)

        return False


sol = Solution()
nums = [1, 0, 1, 1]
k = 1
print(sol.containsNearbyDuplicate(nums, k))
