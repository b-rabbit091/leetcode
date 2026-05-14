'''


17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter

combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
'''


from typing import List


class Solution:
    mp = {"2": ['a', 'b', 'c'],
          "3": ['d', 'e', 'f'],
          "4": ['g', 'h', 'i', ],
          '5': ['j', 'k', 'l'],
          '6': ['m', 'n', 'o'],
          '7': ['p', 'q', 'r', 's'],
          '8': ['t', 'u', 'v'],
          '9': ['w', 'x', 'y', 'z']}

    def solve(self, list_index, res, s, mp_list):
        if len(mp_list) == list_index:
            res.append(s)
            return

        for digit in mp_list[list_index]:
            s += digit
            self.solve(list_index + 1, res, s, mp_list)
            s = s[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        mp_list = []
        for digit in digits:
            mp_list.append(self.mp[digit])
        res = []
        s = ''
        self.solve(0, res, s, mp_list)
        return res


obj = Solution()
digits = "234"
print(obj.letterCombinations(digits))
