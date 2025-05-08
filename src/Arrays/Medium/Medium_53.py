from typing import List


class Solution:

    def solve(self, index, nums, mini):
        if mini[index] != -1:
            return mini[index]
        if index == len(nums) - 1:
            return nums[index]
        mini[index] = max(nums[index], nums[index] + self.solve(index + 1, nums, mini))
        return mini[index]

    def maxSubArray(self, nums: List[int]) -> int:
        k = set()
        mini = [-1] * len(nums)
        for i in range(len(nums)):
            k.add(self.solve(i, nums, mini))
        return max(k)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
print(sol.maxSubArray(nums))
