'''

647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

'''


class Solution:

    def isPalindrome(self, st,left,right,dp):


        if dp.get((left,right),0)!=0:
            return dp[(left,right)]


        if left>=right:
            return True
        if st[left]==st[right]:
            dp[(left,right)]= self.isPalindrome(st,left+1, right-1,dp)
            return dp[(left,right)]
        else:
            return False

    def solve(self, left, right, dp, s):

        if left >= len(s):
            return 0
        count=0

        for ind in range(left, right):
            if self.isPalindrome(s , left, ind,dp):
                count += 1

        count += self.solve(left + 1, right, dp, s)
        return count

    def countSubstrings(self, s: str) -> int:

        if len(s)==1:
            return 1

        left = 0
        dp = {}
        res = self.solve(left, len(s), dp, s)
        return res


s = "aaa"
sol = Solution()
print(sol.countSubstrings(s))

tests = [
    ("abc", 3),
    ("aaa", 6),
    ("a", 1),
    ("aa", 3),
    ("ab", 2),
    ("aba", 4),
    ("abba", 6),
    ("racecar", 10),
    ("aaaa", 10),
    ("banana", 10),
]

sol = Solution()
correct = 0

for s, expected in tests:
    result = sol.countSubstrings(s)

    if result == expected:
        correct += 1

    print(s, "=>", result, "expected:", expected)

print("Correct:", correct, "/", len(tests))

