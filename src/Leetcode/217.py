from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False


nums = [1, 2, 3, 5]
sol = Solution()
print(sol.containsDuplicate(nums))
