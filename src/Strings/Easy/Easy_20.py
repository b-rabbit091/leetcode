class Solution:
    mp = {")": "(",
          "}": "{",
          "]": "["}

    def isValid(self, s: str) -> bool:
        lt = list()
        if len(s) in [0, 1]:
            return False
        for i in s:
            if i in ("(", "{", "["):
                lt.append(i)
            else:
                cb = self.mp.get(i)
                if len(lt) > 0 and lt[-1] == cb:
                    lt = lt[:-1]
                else:
                    return False
        return True if len(lt)==0 else False


sol = Solution()
s = ")}}{{"
print(sol.isValid(s))
