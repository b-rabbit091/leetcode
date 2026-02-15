'''
1190. Reverse Substrings Between Each Pair of Parentheses

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.


'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for item in s:
            if item == ")":
                res = []
                while stk[len(stk) - 1] != "(":
                    res.append(stk.pop())
                stk.pop()
                for i in res:
                    stk.append(i)
            else:
                stk.append(item)
        return "".join(stk)


s = "(abcd)"
sol = Solution()
print(sol.reverseParentheses(s))
# Many test cases loop (correct/false count)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for item in s:
            if item == ")":
                res = []
                while stk[-1] != "(":
                    res.append(stk.pop())
                stk.pop()
                for i in res:
                    stk.append(i)
            else:
                stk.append(item)
        return "".join(stk)


tests = [
    ("(abcd)", "dcba"),
    ("(u(love)i)", "iloveu"),
    ("(ed(et(oc))el)", "leetcode"),
    ("a(bc)de", "acbde"),
    ("(a(bc)d)", "dbca"),
    ("x(yz)", "xzy"),
    ("(ab)(cd)", "badc"),
    ("a(b(cd)e)f", "aedcbf"),
    ("((abc))", "abc"),
    ("(a)", "a"),
    ("(ab(c)d)", "dcba"),
    ("(a(bc)(de)f)", "fedcba"),
    ("z(a(b(c)d)e)f", "zedcbaf"),
    ("(pq(rs)t)", "tsrqp"),
    ("a(bc(def)g)h", "agfedcbh"),
    ("(x(y(z)))", "zyx"),
    ("m(n(op)q)r", "mqponr"),
    ("(hello)", "olleh"),
    ("(a(b(c(d)e)f)g)", "gfedcba"),
    ("(one(two)three)", "eerhtowteno"),
    ("(a(bc)d(ef)g)", "dcbafeg"),
    ("((x))", "x"),
    ("(ab(cd(ef)gh)ij)", "jihgfe d cba"),  # tricky expected might fail
]

sol = Solution()
correct = 0
wrong = 0

for s, expected in tests:
    output = sol.reverseParentheses(s)
    if output == expected:
        correct += 1
    else:
        wrong += 1
    print(f"Input: {s} | Output: {output} | Expected: {expected}")

print("\nTotal Correct:", correct)
print("Total Wrong:", wrong)
