'''
1930. Unique Length-3 Palindromic Subsequences

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with
some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

'''


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mp = {}
        count = 0
        for idx, val in enumerate(s):

            first, last = mp.get(val, [-1, -1])
            if first == -1:
                first = idx
            last = idx
            mp[val] = [first, last]

        for val in mp:
            first, last = mp[val]
            unique_chars = len(set(s[first + 1:last]))
            count += unique_chars
        return count


# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         cmap = {}
#         imap = {}
#         count = 0
#         iset=set()
#         rmap = set()
#         for idx, val in enumerate(s):
#             if cmap.get(val, 0) > 1:
#                 st = val * 3
#                 if st not in rmap:
#                     rmap.add(st)
#                     count += 1
#             if val in iset and idx - imap.get(val, 0) >= 2:
#                 mid_chars = set(s[imap[val] + 1:idx])
#                 for ch in mid_chars:
#                     st = val + ch + val
#                     if st not in rmap:
#                         rmap.add(st)
#                         count += 1
#             cmap[val] = cmap.get(val, 0) + 1
#             imap[val] = idx
#             iset.add(val)
#         return count


s = "bbcbaba"
sol = Solution()
print(sol.countPalindromicSubsequence(s))
