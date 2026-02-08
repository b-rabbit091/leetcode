'''

1358. Number of Substrings Containing All Three Characters

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters
a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
Example 3:

Input: s = "abc"
Output: 1

'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        count = 0
        mp = {}

        while right < len(s):
            mp[s[right]] = mp.get(s[right], 0) + 1
            while mp.get('a', 0) > 0 and mp.get('b', 0) > 0 and mp.get('c', 0) > 0:
                count += len(s) - right
                mp[s[left]] -= 1
                left += 1
            right += 1

        return count


sol = Solution()
s = "abcabc"
print(sol.numberOfSubstrings(s))


def brute_expected(s: str) -> int:
    n = len(s)
    ans = 0
    for i in range(n):
        a = b = c = 0
        for j in range(i, n):
            ch = s[j]
            if ch == 'a':
                a = 1
            elif ch == 'b':
                b = 1
            else:
                c = 1
            if a and b and c:
                ans += 1
    return ans


tests = [
    "abc", "cba", "abcabc", "aaacb", "aabc", "abca", "abcc", "aabbcc",
    "aaaaaa", "bbbbbb", "cccccc",
    "aab", "abb", "acc", "bbb", "cab", "bca",
    "aaabbbccc", "abcabcabc", "acbacb", "cabc", "bbacaa", "ccab",
    "a" * 10 + "b" * 10 + "c" * 10,
    "abc" * 20,
    "abccbaabc",
    "bacacb",
    "aaabcbc",
    "ccbaaaabbbcc",
]

sol = Solution()

for i, s in enumerate(tests, 1):
    expected = brute_expected(s)
    got = sol.numberOfSubstrings(s)
    print(f"Test {i}: s={s!r} (len={len(s)})")
    print("Expected:", expected)
    print("Got     :", got)
    print("Correct :", got == expected)
    print("-" * 60)
