class Solution:
    romans = [[1, "I"],
              [4, "IV"],
              [5, "V"],
              [9, "IX"],
              [10, "X"],
              [40, "XL"],
              [50, "L"],
              [90, "XC"],
              [100, "C"],
              [400, "CD"],
              [500, "D"],
              [900, "CM"],
              [1000, "M"]]

    def intToRoman(self, num: int) -> str:
        sx = ''
        for n, s in reversed(self.romans):
            count = num // n
            if count > 0:
                sx = sx + s*count
                num = num % n
        return sx


sol = Solution()
num = 3
print(sol.intToRoman(num))
