'''

1849. Splitting a String Into Descending Consecutive Values

You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such that the numerical values
 of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89].
The values are in descending order and adjacent values differ by 1, so this way is valid.
Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"].
However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively,
all of which are not in descending order.
Return true if it is possible to split s as described above, or false otherwise.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.
Example 2:

Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.
Example 3:

Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.

'''

from typing import List


class Solution:

    def solve(self, ind, s, prev):

        if ind >= len(s) and prev != s:
            return True

        for i in range(ind, len(s)):
            curr = s[ind:i + 1]
            if len(prev) == 0 or (len(prev) > 0 and int(prev) - int(curr) == 1):
                if self.solve(i + 1, s, curr):
                    return True
        return False

    def splitString(self, s: str) -> bool:
        st = ''
        return self.solve(0, s, st)

test_cases = [
    ("1234", False),
    ("050043", True),
    ("9080701", False),
    ("10009998", True),

    ("1", False),
    ("10", True),
    ("21", True),
    ("32", True),
    ("43", True),
    ("11", False),
    ("01", False),

    ("54321", True),
    ("654321", True),
    ("987654321", True),
    ("1098", True),
    ("111098", True),
    ("1009998", True),
    ("99989796", True),

    ("09998", True),
    ("0090089", True),
    ("000", False),
    ("001", False),
    ("0001", False),

    ("9875", False),
    ("101", False),
    ("10098", False),
    ("999999", False),
    ("12345", False),
    ("10009997", False),
]


sol = Solution()

for i, (s, expected) in enumerate(test_cases, 1):
    output = sol.splitString(s)

    if output == expected:
        print(f"Test {i}: RIGHT | s='{s}' | output={output}")
    else:
        print(f"Test {i}: WRONG | s='{s}'")
        print(f"  Your output: {output}")
        print(f"  Expected:    {expected}")
        print()