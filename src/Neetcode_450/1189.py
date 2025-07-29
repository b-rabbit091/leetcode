'''

1189. Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp = dict()
        base = set("balloon")
        sp=set()

        for i in base:
            mp[i] = 0
        for i in text:
            if i in base:
                ad = 1
                if i in ["l", "o"]:
                    ad = 0.5
                mp[i] = mp.get(i, 0) + ad
        res = int(min(set(mp.values())))
        return res


sol = Solution()
text = "lloo"
print(sol.maxNumberOfBalloons(text))
