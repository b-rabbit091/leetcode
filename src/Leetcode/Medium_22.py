'''
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''
from typing import List


class Solution:
    bl = ["(", ")"]
    mp = {")": "("}

    def isValid(self, s: str) -> bool:
        lt = list()
        if len(s) in [0, 1]:
            return False
        for i in s:
            if i in "(":
                lt.append(i)
            else:
                cb = self.mp.get(i)
                if len(lt) > 0 and lt[-1] == cb:
                    lt = lt[:-1]
                else:
                    return False
        return True if len(lt) == 0 else False

    def solveGenerateParenthesis(self, l, res, n, c, s):
        if c == (n * 2):
            if self.isValid(res):
                l.append(res)
            return
        for b in self.bl:
            res = res + b
            self.solveGenerateParenthesis(l, res, n, c + 1, s)
            res = res[:-1]

        return []

    def generateParenthesis(self, n: int) -> List[str]:
        l = list()
        self.solveGenerateParenthesis(l, '', n, 0, 0)
        return l


sol = Solution()
n = 2
print(sol.generateParenthesis(n))
