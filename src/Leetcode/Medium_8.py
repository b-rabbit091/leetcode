class Solution:
    def myAtoi(self, s: str) -> int:
        count = 0
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] in ('-', '+'):
            count += 1
        al = set()
        k = 0

        while k < 10:
            asc = ascii(k + int(ascii(0)))
            al.add(asc)
            k += 1

        while count < len(s):
            if s[count] in al:
                count += 1
            else:
                break

        if count == 0 or count == 1 and s[0] in ('-', '+'):
            return 0
        res = int(s[0:count])
        if res < pow(-2, 31):
            res = pow(-2, 31)
        elif res > (pow(2, 31) - 1):
            res = pow(2, 31) - 1
        return res


sol = Solution()
#print(sol.myAtoi("-++42"))
