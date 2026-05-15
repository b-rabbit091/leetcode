'''

1593. Split a String Into the Max Number of Unique Substrings

Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings,
where the concatenation of the substrings forms the original string.
However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

'''


class Solution:

    def solve(self, ind, st, curr, res, s):

        if ind == len(s):
            res = max(res, len(curr))
            return res

        for i in range(ind, len(s)):
            st = s[ind:i + 1]
            if st not in curr:
                curr.add(st)
                res = self.solve(i + 1, st, curr, res, s)
                curr.remove(st)
        return res

    def maxUniqueSplit(self, s: str) -> int:
        curr = set()
        res = 0
        st = ""
        ind = 0
        res=self.solve(ind, st, curr, res, s)
        return res


sol = Solution()
s = "aa"
print(sol.maxUniqueSplit(s))
test_cases = [
    ("ababccc", 5),
    ("aba", 2),
    ("aa", 1),
    ("abc", 3),
    ("abab", 3),
    ("aaaa", 2),
    ("abcdef", 6),
    ("wwwzfvedwfvhsww", 11),
    ("addbsd", 5),
    ("leetcode", 7),
    ("abcabc", 4),
    ("aab", 2),
    ("abac", 3),
    ("zzzzz", 2),
    ("pqrst", 5),
]


sol = Solution()

for i, (s, expected) in enumerate(test_cases, 1):
    output = sol.maxUniqueSplit(s)

    if output == expected:
        print(f"Test {i}: RIGHT | s='{s}' | output={output}")
    else:
        print(f"Test {i}: WRONG | s='{s}'")
        print(f"  Your output: {output}")
        print(f"  Expected:    {expected}")
        print()