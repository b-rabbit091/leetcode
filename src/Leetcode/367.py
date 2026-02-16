'''

367. Valid Perfect Square

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.



Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num + 1
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


sol = Solution()
num = 36
print(sol.isPerfectSquare(num))
