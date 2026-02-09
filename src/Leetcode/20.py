'''

20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

'''

class Solution:

    def isValid(self, s: str) -> bool:
        mp = {")": "(", "}": "{", "]": "["}

        stack = []

        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                close_bracket = mp.get(i)
                if len(stack) > 0 and stack[len(stack) - 1] == close_bracket:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


sol = Solution()
s = ")}}{{"
print(sol.isValid(s))

# Test cases for Leetcode 20: Valid Parentheses

tests = [
    # Basic valid cases
    ("()", True),
    ("[]", True),
    ("{}", True),
    ("()[]{}", True),
    ("{[]}", True),
    ("([])", True),
    ("((()))", True),

    # Basic invalid cases
    ("(]", False),
    ("([)]", False),
    ("(((", False),
    (")))", False),
    ("{[}", False),

    # Mixed invalid ordering
    ("{[(])}", False),
    ("((])", False),

    # Starts with closing
    (")", False),
    ("]", False),
    ("}", False),

    # Ends with opening
    ("(", False),
    ("[", False),
    ("{", False),

    # Complex valid
    ("{[()()]}()", True),
    ("((({{{[[[]]]}}})))", True),

    # Complex invalid
    ("{[()()]}", True),
    ("{[()()]}(", False),
    ("{[()()]}}", False),

    # Empty string
    ("", True),

    # Random invalid strings
    (")}}{{", False),
    ("{}}{", False),
    ("[{}}]", False),
]

sol = Solution()

for i, (s, expected) in enumerate(tests, 1):
    result = sol.isValid(s)
    print(f"Test {i}: s={s!r}")
    print("Expected:", expected)
    print("Got     :", result)
    print("Correct :", result == expected)
    print("-" * 50)
