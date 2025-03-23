'''
Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
'''
from typing import List


class Solution:
    ntd = {"1": "",
           "2": "abc",
           "3": "def",
           "4": "ghi",
           "5": "jkl",
           "6": "mno",
           "7": "pqrs",
           "8": "tuv",
           "9": "wxyz"}

    def solveLetterComnbinations(self, count, re, ds, lt):

        if count == len(ds):
            return [] if len(ds) == 0 else lt.append(re)

        for i in self.ntd[ds[count]]:
            re = re + i
            self.solveLetterComnbinations(count + 1, re, ds, lt)
            re = re[:-1]
        return lt

    def letterCombinations(self, digits: str) -> List[str]:

        l = []
        self.solveLetterComnbinations(0, '', digits, l)
        return [] if len(l) == 0 else l

# sol = Solution()
# print(sol.letterCombinations("23"))
