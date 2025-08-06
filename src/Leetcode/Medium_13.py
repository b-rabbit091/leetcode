class Solution:
    romans_map = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        i = 0
        n = 0
        while i < len(s):
            ct = s[i]
            nt = ct
            if i + 1 < len(s):
                nt = nt + s[i + 1]
            k = 0
            if nt in self.romans_map.keys():
                k = self.romans_map.get(nt)
                i += 2
            elif ct in self.romans_map.keys():
                k = self.romans_map.get(ct)
                i += 1
            n = n + k
        return n
# sol = Solution()
# print(sol.romanToInt("LXXXVI"))
