'''
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.


Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

'''

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        length = len(flowerbed)
        if length == 1:
            if flowerbed[0] == 0 and n < 2:
                return True
            return False
        count = 0
        for ind, val in enumerate(flowerbed):
            if val == 0:
                if ind - 1 < 0 and flowerbed[ind + 1] == 0:
                    flowerbed[ind] = 1
                    count += 1
                elif ind + 1 >= length and flowerbed[ind - 1] == 0:
                    flowerbed[ind] = 1
                    count += 1
                elif flowerbed[ind - 1] == 0 and flowerbed[ind + 1] == 0:
                    flowerbed[ind] = 1
                    count += 1
            if count == n:
                return True
        return False


flowerbed = [1, 0, 0, 0, 0, 1]
n = 2
sol = Solution()
print(sol.canPlaceFlowers(flowerbed, n))
