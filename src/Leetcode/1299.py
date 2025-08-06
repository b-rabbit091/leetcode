'''
1299. Replace Elements with Greatest Element on Right Side
Easy
Topics
premium lock icon
Companies
Hint
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
 and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

'''

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = arr[len(arr) - 1]
        res = [-1]
        for i in range(len(arr) - 2, -1, -1):
            res.append(maxi)
            maxi = max(maxi, arr[i])
        res.reverse()
        return res


sol = Solution()
arr = [400]
print(sol.replaceElements(arr))
