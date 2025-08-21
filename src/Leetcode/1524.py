'''

1524. Number of Sub-arrays With Odd Sum

Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.


Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

'''
from typing import List


class Solution:
    def isOdd(self, num) -> bool:
        return num % 2 != 0

    def numOfSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        MOD = (10 ** 9) + 7
        even_count = 1
        odd_count = 0
        presum = 0
        count = 0
        for num in arr:
            presum += num

            if presum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                count += even_count
                odd_count += 1
        return count % MOD


arr = [2, 4, 6]
sol = Solution()
print(sol.numOfSubarrays(arr))
