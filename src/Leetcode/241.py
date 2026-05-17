'''

241. Different Ways to Add Parentheses

Given a string expression of numbers and operators, return all possible results from computing
all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.



Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10


'''
from typing import List


class Solution:

    def solve(self, expr, op_map):
        res = []

        for i, ch in enumerate(expr):
            if ch in ['+', '-', '*']:
                left = self.solve(expr[:i], op_map)
                right = self.solve(expr[i + 1:], op_map)
                for num1 in left:
                    for num2 in right:
                        res.append(op_map[ch](num1, num2))

        if not res:
            return [int(expr)]

        else:
            return res

    def diffWaysToCompute(self, expression: str) -> List[int]:
        op_map = {"+": lambda x, y: x + y,
                  "-": lambda x, y: x - y,
                  "*": lambda x, y: x * y}
        res = self.solve(expression, op_map)

        return res


sol = Solution()
expression = "2*3-4*5"
print(sol.diffWaysToCompute(expression))
