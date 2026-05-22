'''

2707. Extra Characters in a String


You are given a 0-indexed string s and a dictionary of words dictionary.
You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary.
There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8.
There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12.
The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

'''

from typing import List


class Solution:

    def solve(self, ind, s, set_wordDict, dp):

        if dp.get(ind, -1) != -1:
            return dp[ind]
        if ind >= len(s):
            return 0
        mini=float('inf')
        for i in range(ind, len(s)):
            st = s[ind:i + 1]
            if st in set_wordDict:
                mini = min(mini,self.solve(i + 1, s, set_wordDict, dp))
        dp[ind]=min(mini,1 + self.solve(ind + 1, s, set_wordDict, dp))
        return dp[ind]

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ind = 0
        set_wordDict = set(dictionary)
        dp = {}
        return self.solve(ind, s, set_wordDict, dp)


sol = Solution()
s = "ecolloycollotkvzqpdaumuqgs"
dictionary = ["flbri", "uaaz", "numy", "laper", "ioqyt", "tkvz", "ndjb", "gmg", "gdpbo", "x", "collo", "vuh", "qhozp",
              "iwk", "paqgn", "m", "mhx", "jgren", "qqshd", "qr", "qpdau", "oeeuq", "c", "qkot", "uxqvx", "lhgid",
              "vchsk", "drqx", "keaua", "yaru", "mla", "shz", "lby", "vdxlv", "xyai", "lxtgl", "inz", "brhi", "iukt",
              "f", "lbjou", "vb", "sz", "ilkra", "izwk", "muqgs", "gom", "je"]
print(sol.minExtraChar(s, dictionary))
sol = Solution()
tests = [
    (
        "ecolloycollotkvzqpdaumuqgs",
        [
            "flbri", "uaaz", "numy", "laper", "ioqyt", "tkvz", "ndjb", "gmg",
            "gdpbo", "x", "collo", "vuh", "qhozp", "iwk", "paqgn", "m", "mhx",
            "jgren", "qqshd", "qr", "qpdau", "oeeuq", "c", "qkot", "uxqvx",
            "lhgid", "vchsk", "drqx", "keaua", "yaru", "mla", "shz", "lby",
            "vdxlv", "xyai", "lxtgl", "inz", "brhi", "iukt", "f", "lbjou",
            "vb", "sz", "ilkra", "izwk", "muqgs", "gom", "je"
        ],
        2
    ),

    ("leetscode", ["leet", "code", "leetcode"], 1),

    ("sayhelloworld", ["hello", "world"], 3),

    ("applepie", ["apple", "pie"], 0),

    ("applexyzpie", ["apple", "pie"], 3),

    ("catsandog", ["cats", "dog", "sand", "and", "cat"], 2),

    ("abcd", ["abc", "b", "cd"], 1),

    ("abcd", ["abc", "a", "bcd"], 0),

    ("abcde", ["abc", "bcde", "a"], 0),

    ("aaaaab", ["a", "aa", "aaa"], 1),

    ("aaaaab", ["aaa", "aab", "aaaa"], 0),

    ("abcxabc", ["abc"], 1),

    ("nepalxriverxyprotection", ["nepal", "river", "protection"], 3),

    ("programmingx", ["program", "ming", "programming"], 1),

    ("xprogrammingy", ["program", "ming", "programming"], 2),

    ("abcdef", ["x", "y", "z"], 6),

    ("Applepie", ["apple", "pie"], 5),

    ("leetcode", ["leet", "code"], 0),

    ("leetcode", ["leet", "cod"], 1),

    ("abcabc", ["abc"], 0),

    ("abcxabcx", ["abc"], 2),

    ("zzzzz", ["a", "b", "c"], 5),

    ("a", ["a"], 0),

    ("a", ["b"], 1),
]

sol = Solution()

for s, dictionary, expected in tests:
    result = sol.minExtraChar(s, dictionary)
    print(s, result, "expected:", expected, result == expected)