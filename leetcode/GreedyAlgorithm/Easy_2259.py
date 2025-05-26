class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        s = set()
        for i in range(len(number)):
            if number[i] is digit:
                ele = number[:i] + number[i + 1:]
                if len(ele) > 0:
                    s.add(int(ele))

        return str(max(s))


number = "123"
digit = "3"
sol = Solution()
print(sol.removeDigit(number, digit))
