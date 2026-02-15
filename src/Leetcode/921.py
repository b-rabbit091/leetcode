'''
921. Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.



Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
'''


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        for item in s:
            if item == "(":
                stk.append(item)
            else:
                if stk and stk[len(stk) - 1] == "(" and item == ")":
                    stk.pop()
                else:
                    stk.append(item)
        return len(stk)


sol = Solution()
s = "((("
print(sol.minAddToMakeValid(s))
tests = [
    ("()", 0),
    ("(((", 3),
    (")))", 3),
    ("(()", 1),
    ("())", 1),
    ("()))((", 4),
    ("(())", 0),
    ("())(()", 2),
    ("())())", 2),
    ("(()())", 0),
    ("()()()", 0),
    ("((())", 1),
    (")()(", 2),
    ("())((())", 2),
    ("", 0),
    ("(((((()", 5),
    ("(()))(()", 2),
    ("())())())", 3),
    ("((()))", 0),
    ("())(()))(", 3),
]

sol = Solution()
correct = 0
wrong = 0

for s, expected in tests:
    output = sol.minAddToMakeValid(s)
    if output == expected:
        correct += 1
    else:
        wrong += 1
    print(f"Input: {s} | Output: {output} | Expected: {expected}")

print("\nTotal Correct:", correct)
print("Total Wrong:", wrong)
