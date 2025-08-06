from typing import List
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        right = len(colors) - 1
        left = 0

        while colors[0] == colors[right]:
            right -= 1
        right_d = right

        while colors[len(colors) - 1] == colors[left]:
            left += 1

        left_d = len(colors) - 1 - left

        diff = max(right_d,left_d)
        return diff


sol = Solution()
colors = [0,1]
print(sol.maxDistance(colors))
