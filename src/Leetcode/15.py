'''

15. 3Sum

Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

'''

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_res = []
        duplicate_set = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right] + nums[i]
                if curr_sum == 0:
                    curr_res = [nums[left], nums[right], nums[i]]
                    curr_res.sort()
                    if tuple(curr_res) not in duplicate_set:
                        duplicate_set.add(tuple(curr_res))
                        final_res.append(curr_res)
                    left += 1
                    right -= 1

                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
        return final_res


nums = [-2, 0, 0, 2, 2]
sol = Solution()

print(sol.threeSum(nums))
