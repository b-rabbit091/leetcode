from typing import List


class Solution:

    def f(self, n, l):
        if n == 2:
            return [1, 1]

        if self.l.get(n) is not None:
            return l[n]

        self.l[n - 1] = (self.f(n - 1, self.l))
        a = []
        for i in range(n):
            elem = 1 if i == 0 or i == n - 1 else self.l[n - 1][i - 1] + self.l[n - 1][i]
            a.append(elem)
        self.l[n] = a
        return a

    def generate(self, numRows: int) -> List[List[int]]:
        self.l = dict()
        self.l[1] = [1]
        self.f(numRows, self.l)
        return list(self.l.values())


s = Solution()
s.generate(5)
