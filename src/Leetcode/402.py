'''
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.



Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


'''


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        stk = []
        count = k
        for st in num:
            while stk and stk[len(stk) - 1] > st and count > 0:
                stk.pop()
                count -= 1
            stk.append(st)
        while stk and count > 0:
            stk.pop()
            count -= 1
        res = "".join(stk)
        return res if res.lstrip("0") else "0"


sol = Solution()
num = "1001"
k = 1
print(sol.removeKdigits(num, k))
tests = [
    ("1432219", 3, "1219"),
    ("10200", 1, "200"),
    ("10", 2, "0"),
    ("9", 1, "0"),
    ("112", 1, "11"),
    ("123456", 3, "123"),
    ("654321", 3, "321"),
    ("10001", 1, "1"),
    ("10001", 2, "0"),
    ("765028321", 5, "221"),
    ("1111111", 3, "1111"),
    ("1000", 1, "0"),
    ("1000", 2, "0"),
    ("12345", 1, "1234"),
    ("54321", 1, "4321"),
]

sol = Solution()
passed = 0

for i, (num, k, expected) in enumerate(tests, 1):
    got = sol.removeKdigits(num, k)
    ok = got == expected
    print(f"Test {i}: num={num}, k={k}")
    print(f"Expected: {expected}")
    print(f"Got     : {got}   {'✅ Correct' if ok else '❌ Incorrect'}\n")
    if ok:
        passed += 1

print(f"Passed {passed}/{len(tests)} tests")
