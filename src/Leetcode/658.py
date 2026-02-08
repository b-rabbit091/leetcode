'''

658. Find K Closest Elements
Medium
Topics
premium lock icon
Companies
Given a sorted integer array arr, two integers k and x,
return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]


'''

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        mp = {}
        right = 0
        sumi = float('inf')
        fin = 0
        left = 0

        while right < len(arr):
            mp[arr[right]] = mp.get(arr[right], 0) + abs(arr[right] - x)
            while right - left + 1 >= k:
                curr_sum = sum(mp.values())
                if curr_sum < sumi:
                    fin = arr[left:right + 1]
                    sumi = curr_sum
                updated_value = mp[arr[left]] - abs(arr[left] - x)
                mp[arr[left]] = updated_value
                left += 1
            right += 1
        return fin


sol = Solution()
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(sol.findClosestElements(arr, k, x))

# Test cases for Leetcode 658: Find K Closest Elements

tests = [
    # Examples
    ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
    ([1, 1, 2, 3, 4, 5], 4, -1, [1, 1, 2, 3]),

    # Edge cases
    ([1], 1, 10, [1]),
    ([1, 2], 1, 1, [1]),
    ([1, 2], 1, 2, [2]),
    ([1, 2], 2, 100, [1, 2]),

    # x smaller than all
    ([2, 3, 4, 5, 6], 3, -10, [2, 3, 4]),

    # x larger than all
    ([2, 3, 4, 5, 6], 3, 100, [4, 5, 6]),

    # x exactly present
    ([1, 2, 3, 4, 5], 2, 3, [2, 3]),

    # tie-breaking (prefer smaller values)
    ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 4, 4, [2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 2, 3, [2, 3]),
    ([1, 2, 3, 4, 5], 2, 3, [2, 3]),

    # duplicates around x
    ([1, 2, 2, 2, 3, 4], 3, 2, [2, 2, 2]),
    ([1, 1, 1, 2, 2, 2, 3], 4, 2, [1, 2, 2, 2]),

    # k = len(arr)
    ([1, 2, 3, 4], 4, 10, [1, 2, 3, 4]),
    ([1, 2, 3, 4], 4, -10, [1, 2, 3, 4]),

    # tight middle windows
    ([1, 3, 3, 3, 5, 7, 9], 3, 4, [3, 3, 5]),
    ([1, 2, 3, 4, 4, 4, 5, 6], 3, 4, [4, 4, 4]),

    # more ties
    ([1, 2, 3, 4], 2, 2, [1, 2]),
    ([1, 2, 3, 4], 2, 3, [2, 3]),
]

sol = Solution()

for i, (arr, k, x, expected) in enumerate(tests, 1):
    result = sol.findClosestElements(arr, k, x)
    print(f"Test {i}: arr={arr}, k={k}, x={x}")
    print("Expected:", expected)
    print("Got     :", result)
    print("Correct :", result == expected)
    print("-" * 60)
