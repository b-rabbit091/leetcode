'''
735. Asteroid Collision
Medium
Topics
premium lock icon
Companies
Hint
We are given an array asteroids of integers representing asteroids in a row.
The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents
its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [3,5,-6,2,-1,4]
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left.
On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.
'''

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            flag = True
            while flag and (stk and stk[len(stk) - 1] > 0 > ast):
                if abs(stk[len(stk) - 1]) < abs(ast):
                    stk.pop()
                elif abs(stk[len(stk) - 1]) == abs(ast):
                    stk.pop()
                    flag = False
                else:
                    flag = False
            if flag:
                stk.append(ast)
        return stk


sol = Solution()
asteroids = [5, 10, -5]
print(sol.asteroidCollision(asteroids))

tests = [
    # Given examples
    ([5, 10, -5], [5, 10]),
    ([8, -8], []),
    ([10, 2, -5], [10]),
    ([3, 5, -6, 2, -1, 4], [-6, 2, 4]),

    # No collisions (all same direction)
    ([1, 2, 3], [1, 2, 3]),
    ([-1, -2, -3], [-1, -2, -3]),

    # Simple collisions
    ([4, -2], [4]),
    ([2, -4], [-4]),
    ([1, -1], []),

    # Chain collisions
    ([1, 2, 3, -10], [-10]),
    ([10, -1, -2, -3], [10]),
    ([5, 10, -20], [-20]),
    ([6, 3, -4], [6]),

    # Multiple equal-size wipes
    ([2, 2, -2], [2]),
    ([2, 2, -2, -2], []),

    # Tricky sequences
    ([-2, -1, 1, 2], [-2, -1, 1, 2]),  # never meet
    ([1, -2, -2, -2], [-2, -2, -2]),
    ([7, 1, 2, -3, -8], [-8]),
    ([3, 4, -2, -2, -5], [-5]),
    ([10, 5, -5, -20], [-20]),
]

passed = 0
for i, (inp, expected) in enumerate(tests, 1):
    got = sol.asteroidCollision(inp)
    ok = got == expected
    passed += ok
    print(f"Test {i:02d}: input={inp}")
    print(f"  expected: {expected}")
    print(f"  got     : {got}   {'✅ correct' if ok else '❌ incorrect'}\n")

print(f"Passed {passed}/{len(tests)} tests ({passed / len(tests) * 100:.1f}%).")
