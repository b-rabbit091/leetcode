'''

2375. Construct Smallest Number From DI String

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.



Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.

'''


class Solution:

    def solve(self, ind, pattern, curr, res):

        if len(curr) == len(pattern) + 1:
            res = curr
            return res

        for i in range(1, 10):
            if (((len(curr) == 0) or
                    (ind - 1 >= 0 and ind <= len(pattern) and pattern[ind - 1] == 'I' and int(curr[-1]) < i)
                    or (ind - 1 >= 0 and ind <= len(pattern) and pattern[ind - 1] == "D" and int(curr[-1]) > i)
                    )  and str(i) not in curr ):
                curr += str(i)
                res = self.solve(ind + 1, pattern, curr, res)
                if res != '':
                    return res
                curr = curr[:-1]
        return res

    def smallestNumber(self, pattern: str) -> str:
        curr = ""
        res = ''
        k = self.solve(0, pattern, curr, res)
        return k


sol = Solution()
pattern = "IIIDIDDD"
test_cases = [
    ("IIIDIDDD", "123549876"),
    ("DDD", "4321"),
    ("III", "1234"),
    ("D", "21"),
    ("I", "12"),
    ("ID", "132"),
    ("DI", "213"),
    ("IID", "1243"),
    ("DDI", "3214"),
    ("DID", "2143"),
    ("IDI", "1324"),
    ("DDDD", "54321"),
    ("IIII", "12345"),
    ("DIDI", "21435"),
    ("IDID", "13254"),
    ("IIDDD", "126543"),
    ("DDIID", "321465"),
]


sol = Solution()

for i, (pattern, expected) in enumerate(test_cases, 1):
    output = sol.smallestNumber(pattern)

    if output == expected:
        print(f"Test {i}: RIGHT | pattern='{pattern}' | output={output}")
    else:
        print(f"Test {i}: WRONG | pattern='{pattern}'")
        print(f"  Your output: {output}")
        print(f"  Expected:    {expected}")
        print()