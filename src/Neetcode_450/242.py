'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
using all the original letters exactly once.
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return sorted(s)==sorted(t)

        if len(s) != len(t):
            return False
        maps = dict()
        s.count("a")
        for i in s:
            maps[i] = maps.get(i, 0) + 1
        for j in t:
            if j not in maps.keys():
                return False
            maps[j] = maps.get(j, 0) - 1
            if maps[j]==0:
                return False
        return True


sol = Solution()
s = "anagram"
t = "nagaram"
print(sol.isAnagram(s, t))
