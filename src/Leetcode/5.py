'''

5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''


class Solution:

    def isPalindrome(self, s, dp, low, high):

        if low >= high:
            return True

        if (low,high) in dp.keys():
            return dp[(low,high)]

        if s[low] == s[high]:
            dp[(low, high)] = self.isPalindrome(s, dp, low + 1, high - 1)
        else:
            dp[(low, high)] = False
        return dp[(low, high)]

    def solve(self, ind, s, res, dp):
        if ind >= len(s):
            return res
        for i in range(ind, len(s)):
            if self.isPalindrome(s, dp, ind, i):
                st = s[ind:i + 1]
                if len(st) > len(res):
                    res = st
        res2 = self.solve(ind + 1, s, res, dp)
        return res if len(res) > len(res2) else res2

    def longestPalindrome(self, s: str) -> str:
        ind = 0
        res = []
        dp = {}
        return self.solve(ind, s, res, dp)


tests = [
    ("babad", "bab or aba"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("ac", "a or c"),
    ("bada", "ada"),
    ("racecar", "racecar"),
    ("aaaa", "aaaa"),
    ("abcda", "a or b or c or d"),
    ("bananas", "anana"),
    ("forgeeksskeegfor", "geeksskeeg"),
]

sol = Solution()

for s, expected in tests:
    print(s, "=>", sol.longestPalindrome(s), "expected:", expected)
