'''
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "acb", t = "ahbgdc"
Output: true

'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        ptr = 0
        for i in t:
            if ptr < len(s) and s[ptr] == i:
                ptr += 1

        return ptr == len(s)


sol = Solution()
s = "a"
t = "baaaaa"
print(sol.isSubsequence(s, t))
