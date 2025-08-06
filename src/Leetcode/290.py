'''
290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true
'''


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strps = s.split(" ")
        ptos = {}
        stop = {}
        if len(pattern) != len(strps):
            return False
        for idx, val in enumerate(pattern):
            if ptos.get(val, -1) == -1 and stop.get(strps[idx], -1) == -1:
                ptos[val] = strps[idx]
                stop[strps[idx]] = val
            elif ptos.get(val) != strps[idx]:
                return False
            elif stop[strps[idx]] != val:
                return False
        return True


sol = Solution()
pattern = "abc"
s = "b c a"
print(sol.wordPattern(pattern, s))
