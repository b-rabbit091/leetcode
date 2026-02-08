'''
1208. Get Equal Substrings Within Budget

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e.,
the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding
substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed
to its corresponding substring from t, return 0.



Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.
'''

from typing import List


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        right = 0
        maxi = -float('inf')
        left = 0
        diff = maxCost
        while right < len(s):
            curr_diff = (abs(ord(s[right]) - ord(t[right])))
            diff = diff - curr_diff
            while diff < 0:
                diff += (abs(ord(s[left]) - ord(t[left])))
                left += 1

            maxi = max(maxi, right - left + 1)
            right += 1
        return maxi


sol = Solution()
s = "abcdef"
t = "azcedf"
maxCost = 5
print(sol.equalSubstring(s, t, maxCost))


tests = [
    # Examples
    ("abcd", "bcdf", 3, 3),
    ("abcd", "cdef", 3, 1),
    ("abcd", "acde", 0, 1),

    # Edge cases
    ("a", "b", 0, 0),
    ("a", "a", 0, 1),
    ("a", "z", 25, 1),
    ("a", "z", 24, 0),

    # Full string possible
    ("aaaa", "bbbb", 4, 4),
    ("aaaa", "bbbb", 3, 3),

    # Budget too small
    ("abcd", "zzzz", 1, 0),

    # Large valid prefix but better answer later (sliding window needed)
    ("abcdxyz", "bcdfxyz", 3, 3),

    # Middle substring best
    ("krrgw", "zjxss", 19, 2),

    # Alternating cheap/expensive diffs
    ("abcdef", "azcedf", 5, 3),

    # All equal strings
    ("hello", "hello", 0, 5),

    # One expensive char breaks
    ("aaaaab", "aaaaaz", 1, 5),

    # Best window not starting at index 0
    ("abcd", "abzz", 4, 2),
]

sol = Solution()

for i, (s, t, maxCost, expected) in enumerate(tests, 1):
    result = sol.equalSubstring(s, t, maxCost)
    print(f"Test {i}: s={s}, t={t}, maxCost={maxCost}")
    print("Expected:", expected)
    print("Got     :", result)
    print("Correct :", result == expected)
    print("-" * 60)
