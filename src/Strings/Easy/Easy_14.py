from typing import List


class Solution:
    mp = dict()
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        common = 0
        mi = 201
        for index, value in enumerate(strs):
            if index == 0:
                for ch in value:
                    self.mp[count] = ch
                    count = count + 1
            else:
                c = False
                for ind, ch in enumerate(value):
                    if ch == self.mp[ind]:
                        common = ind
                        c = True
                    else:
                        break
                if not c:
                    return ''
                if common < mi:
                    mi = common
        return strs[0][:mi + 1]
sol = Solution()
print(sol.longestCommonPrefix(["cwg", "cwracecar", "c"]))
