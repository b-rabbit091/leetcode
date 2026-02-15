'''
394 Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces,
square brackets are well-formed, etc. Furthermore, you may assume that the original data
does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''


class Solution:
    def decodeString(self, s: str) -> str:

        stk = []
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for st in s:
            if st == ']':
                k = []
                num =''
                while stk and stk[len(stk) - 1] not in digits:
                    elem = stk.pop()
                    if elem != "[":
                        k.append(elem)

                while stk and stk[len(stk)-1] in digits:
                    num = stk.pop()+num

                k.reverse()
                k = (int(num) if num else 1) * k
                k = "".join(k)
                st = k
            stk.append(st)
        return "".join(stk)


s = "3[a]2[bc]"
sol = Solution()
print(sol.decodeString(s))

tests = [
    ("1[a]", "a"),
    ("2[a]", "aa"),
    ("3[xy]", "xyxyxy"),
    ("4[z]", "zzzz"),
    ("5[mn]", "mnmnmnmnmn"),

    ("2[ab3[c]]", "abcccabccc"),
    ("3[a2[b3[c]]]", "abcccbcccabcccbcccabcccbccc"),
    ("2[x3[y]z]", "xyyyzxyyyz"),
    ("3[p2[q]]", "pqqpqqpqq"),

    ("10[a]", "aaaaaaaaaa"),
    ("11[b]", "bbbbbbbbbbb"),
    ("12[ab]", "abababababababababababab"),
    ("20[x]", "xxxxxxxxxxxxxxxxxxxx"),

    ("2[a]3[b]4[c]", "aabbbcccc"),
    ("3[a]2[bc]1[d]", "aaabcbcd"),
    ("1[a2[b]]", "abb"),

    ("2[2[2[a]]]", "aaaaaaaa"),
    ("3[a10[b]]", "abbbbbbbbbbabbbbbbbbbbabbbbbbbbbb"),
    ("2[abc]2[cd]2[ef]", "abcabccdcdedef"),

    ("7[a]", "aaaaaaa"),
    ("8[xy]", "xyxyxyxyxyxyxyxy"),
    ("9[z2[y]]", "zyyzyyzyyzyyzyyzyyzyyzyyzyyzyy"),
]
sol = Solution()
passed = 0

for i, (inp, expected) in enumerate(tests, 1):
    got = sol.decodeString(inp)
    ok = got == expected
    print(f"Test {i}: s={inp}")
    print(f"Expected: {expected}")
    print(f"Got     : {got}   {'✅ Correct' if ok else '❌ Incorrect'}\n")
    if ok:
        passed += 1

print(f"Passed {passed}/{len(tests)} tests")