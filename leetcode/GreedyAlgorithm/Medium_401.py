class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if len(num) == 0:
            return "0"
        st = []
        for i in num:
            while len(st) > 0 and int(i) < int(st[-1]) and k > 0:
                st.pop()
                k -= 1
            st.append(i)
        while k > 0:
            st.pop()
            k -= 1
        res = "".join(st).lstrip("0")
        return "0" if len(res)==0 else res


sol = Solution()
num = "33526221184202197273"
k = 19
print(sol.removeKdigits(num, k))
