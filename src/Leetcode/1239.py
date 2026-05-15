'''
1239. Maximum Length of a Concatenated String with Unique Characters

You are given an array of strings arr. A string s is formed by the concatenation
of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no
elements without changing the order of the remaining elements.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
'''
from typing import List


class Solution:
    def solve(self, ind, st, curr, res, arr):
        s = "".join(st)
        if len(s) != len(set(s)):
            return res
        res = max(res, len(s))
        for i in range(ind, len(arr)):
            st.append(arr[i])
            res = self.solve(i + 1, st, curr, res, arr)
            st.pop()
        return res

    def maxLength(self, arr: List[str]) -> int:
        ind = 0
        curr = set()
        st = []
        res = 0
        return self.solve(ind, st, curr, res, arr)


sol = Solution()
arr = ["un", "iq", "ue"]
print(sol.maxLength(arr))
test_cases = [
    (["un", "iq", "ue"], 4),
    (["cha", "r", "act", "ers"], 6),
    (["abcdefghijklmnopqrstuvwxyz"], 26),
    (["aa", "bb"], 0),
    (["a", "b", "c"], 3),
    (["ab", "cd", "ef"], 6),
    (["ab", "bc", "cd"], 4),
    (["abc", "def", "gh"], 8),
    (["abc", "ade", "xyz"], 6),
    (["a", "abc", "d", "de", "def"], 6),
    (["a", "aa", "aaa"], 1),
    (["ab", "ba", "cd"], 4),
    (["yy", "bkhwmpbiisbldzknpm"], 0),
    (["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"], 16),
]


sol = Solution()

for i, (arr, expected) in enumerate(test_cases, 1):
    output = sol.maxLength(arr)

    if output == expected:
        print(f"Test {i}: RIGHT | arr={arr} | output={output}")
    else:
        print(f"Test {i}: WRONG | arr={arr}")
        print(f"  Your output: {output}")
        print(f"  Expected:    {expected}")
        print()