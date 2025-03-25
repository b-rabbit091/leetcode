from typing import Any


class Solution:

    def countAndSay(self, n:int)-> str | Any:
        if n == 1:
            return "1"
        else:
            dig = self.countAndSay((n - 1))
            return self.reln(str(dig),'',0)

    def reln(self, n, cstr, index):
        queue = []

        while index < len(n):
            if len(queue) > 0 and n[index] != queue[0]:
                cstr = cstr + str(len(queue)) + queue[0]
                queue.clear()
            queue.append(n[index])
            index = index + 1
        return cstr + str(len(queue)) + queue[0]


# sol = Solution()
# num = 2
# print(sol.countAndSay(num))
