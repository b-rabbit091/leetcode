'''
139. Word Break
Medium
Topics
premium lock icon
Companies
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''

from typing import List


class Solution:
    def solve(self, ind, s, set_wordDict, dp):

        if dp.get(ind, -1) != -1:
            return dp[ind]

        if ind >= len(s):
            return True
        for i in range(ind, len(s)):
            st = s[ind:i + 1]
            if st in set_wordDict:
                if self.solve(i + 1, s, set_wordDict, dp):
                    dp[ind] = True
                    return dp[ind]
        dp[ind] = False
        return dp[ind]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ind = 0
        set_wordDict = set(wordDict)
        dp = {}
        return self.solve(ind, s, set_wordDict, dp)


s = "goalspecial"
wordDict = ["goal", "special"]
sol = Solution()
tests = [
    # 1. Base / Standard Cases
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("cars", ["car", "ca", "rs"], True),
    ("aaaaaaa", ["aaaa", "aaa"], True),
    ("dict", ["dict"], True),

    # 2. Minimum Constraints (Length 1)
    ("a", ["a"], True),
    ("a", ["b"], False),

    # 3. Maximum Word Length Constraint (wordDict[i].length = 20)
    ("abcdefghijklmnopqrst", ["abcdefghijklmnopqrst"], True),
    ("abcdefghijklmnopqrstu", ["abcdefghijklmnopqrst"], False),

    # 4. Overlapping / Misleading Prefixes
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ("ccbb", ["bc", "cb", "c"], False),
    ("goalspecial", ["go", "goal", "special"], True),

    # 5. Large Dictionary Constraint (1000 unique words)
    # Target string is "xyz", dictionary has 999 dummy words plus the actual components
    ("xyz", [f"word{i}" for i in range(997)] + ["xy", "z", "xyz_dummy"], True),

    # 6. Maximum String Length & TLE Trap (s.length = 300, lowercase letters, unique dictionary)
    (
        "a" * 299 + "b",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"],
        False
    )
]

correct = 0

for s, wordDict, expected in tests:
    result = sol.wordBreak(s, wordDict)

    if result == expected:
        correct += 1

    print(s, wordDict, "=>", result, "expected:", expected)

print("Correct:", correct, "/", len(tests))
