'''


739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        vals = []
        indx = []
        stk = [0] * len(temperatures)
        ptr = 0
        while ptr < len(temperatures):
            while vals and temperatures[ptr] > vals[len(vals) - 1]:
                stk[indx[len(indx) - 1]] = ptr - indx[len(indx) - 1]
                vals.pop()
                indx.pop()
            vals.append(temperatures[ptr])
            indx.append(ptr)

            ptr += 1
        return stk

temperatures = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(temperatures))

sol = Solution()

tests = [
    # LeetCode example
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),

    # Strictly increasing
    ([30,40,50,60], [1,1,1,0]),

    # Strictly decreasing
    ([60,50,40,30], [0,0,0,0]),

    # All equal
    ([50,50,50,50], [0,0,0,0]),

    # Single element
    ([100], [0]),

    # Random mix
    ([70,71,69,72], [1,2,1,0]),

    # Late warmer day
    ([80,79,78,77,90], [4,3,2,1,0]),

    # Alternating highs/lows
    ([70,60,70,60,70], [0,1,0,1,0]),

    # Another tricky case
    ([55,56,54,53,57], [1,3,2,1,0]),
]

passed = 0

for i, (inp, expected) in enumerate(tests, 1):
    output = sol.dailyTemperatures(inp)
    correct = output == expected

    print(f"Test {i}: {inp}")
    print(f"Expected: {expected}")
    print(f"Got     : {output}")
    print("✅ Correct\n" if correct else "❌ Incorrect\n")

    if correct:
        passed += 1

print(f"Passed {passed}/{len(tests)} tests")
