'''
91. Decode Ways

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

'''


class Solution:
    low = 96
    high = 123

    def canBeDecode(self, s, dp):

        if s in dp:
            return dp[s]
        if s.startswith("0"):
            dp[s] = False
            return dp[s]
        if len(s) > 2:
            dp[s] = False
            return dp[s]
        ascii1 = self.low + int(s)
        if self.low < ascii1 < self.high:
            dp[s] = True
        else:
            dp[s] = False
        return dp[s]

    def solve(self, left, right, dp, s):

        if left in dp:
            return dp[left]

        if left >= len(s):
            return 1
        res = 0
        for i in range(left, right):
            st = s[left:i + 1]
            if st.startswith("0"):
                dp[st] = False
            if dp.get(st, True):
                if self.canBeDecode(st, dp):
                    res += self.solve(i + 1, right, dp, s)
            dp[left] = res
        return dp[left]

    def numDecodings(self, s: str) -> int:
        left = 0
        dp = {}
        res = self.solve(left, len(s), dp, s)
        return res


import time
import tracemalloc


def run_tests(sol, tests, time_limit=1.0, memory_limit_mb=128):
    correct = 0

    for s, expected in tests:
        tracemalloc.start()
        start = time.perf_counter()

        try:
            result = sol.numDecodings(s)
        except RecursionError:
            print(s, "=> RecursionError")
            tracemalloc.stop()
            continue

        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        runtime = end - start
        memory_mb = peak / (1024 * 1024)

        if runtime > time_limit:
            print(s[:30], "... => TLE", f"time: {runtime:.4f}s")
        elif memory_mb > memory_limit_mb:
            print(s[:30], "... => MLE", f"memory: {memory_mb:.2f}MB")
        else:
            status = "PASS" if result == expected else "FAIL"
            if status == "PASS":
                correct += 1

            print(
                s[:30],
                "=>",
                result,
                "expected:",
                expected,
                status,
                f"time: {runtime:.4f}s",
                f"memory: {memory_mb:.2f}MB"
            )

    print("Correct:", correct, "/", len(tests))


sol = Solution()
s = "11106"
print(sol.numDecodings(s))
tests = [
    ("12", 2),
    ("226", 3),
    ("06", 0),
    ("223", 3),
    ("11106", 2),
    ("2611055971756562", 4),

    # stress tests
    ("1" * 30, 1346269),
    ("1" * 35, 14930352),
    ("1" * 40, 165580141),
    ("1" * 45, 1836311903),
]

sol = Solution()
run_tests(sol, tests, time_limit=1.0, memory_limit_mb=128)
