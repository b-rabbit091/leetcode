'''

205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.


Example 1:

Input: s = "egg", t = "adx"

Output: true
'''


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        new_str = ""
        if len(s) != len(t):
            return False
        for id, key in enumerate(s):
            if t[id] == key:
                char = t[id]
            elif key not in mp.keys():
                mp[key] = t[id]
                char = mp[key]
            else:
                char = mp[key]
            new_str = new_str + char
        if new_str == t:
            new_str = ""
            for id, key in enumerate(t):
                if s[id] == key:
                    char = s[id]
                elif key not in mp.keys():
                    mp[key] = s[id]
                    char = mp[key]
                else:
                    char = mp[key]
                new_str = new_str + char
            return new_str == s
        return False


sol = Solution()
s, t = "paper", "title"
print(sol.isIsomorphic(s, t))
