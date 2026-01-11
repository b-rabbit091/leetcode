'''

11. Container With Most Water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left

            small_height = min(height[right], height[left])
            max_area = max(small_height * width, max_area)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area


sol = Solution()
height = [1, 1]

print(sol.maxArea(height))
