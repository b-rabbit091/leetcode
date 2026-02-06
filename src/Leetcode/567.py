'''

567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ms1 = {}
        dict_keys = set()
        for i in s1:
            ms1[i] = ms1.get(i, 0) + 1
            dict_keys.add(i)

        left = 0
        length = len(s1)
        ms2 = {}

        for right in range(len(s2)):

            ms2[s2[right]] = ms2.get(s2[right], 0) + 1
            if s2[right] not in dict_keys or right - left + 1 > length:
                updated_vale = ms2.get(s2[left], 0) - 1
                if updated_vale == 0:
                    del (ms2[s2[left]])
                else:
                    ms2[s2[left]] = updated_vale

                left += 1

            if ms1 == ms2:
                return True
        return False


sol = Solution()
s1 = "adc"
s2 = "dcda"

print(sol.checkInclusion(s1, s2))
# Test cases (running in loop) with expected answers
tests = [
    # given / basic
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),

    # length edges
    ("a", "a", True),
    ("a", "b", False),
    ("a", "ba", True),
    ("a", "bbbbbbbbbb", False),
    ("ab", "ab", True),
    ("ab", "ba", True),
    ("ab", "a", False),
    ("abcd", "abc", False),

    # s1 longer / s2 shorter
    ("abc", "ab", False),
    ("aa", "a", False),

    # repeated chars in s1
    ("aa", "aa", True),
    ("aa", "aaa", True),
    ("aa", "aba", False),
    ("aab", "aba", True),
    ("aab", "baa", True),
    ("aab", "abb", False),
    ("aabb", "baba", True),
    ("aabb", "bbab", True),
    ("aabb", "abac", False),

    # permutation at start / middle / end
    ("abc", "abcxxxx", True),  # start
    ("abc", "xxcabxx", True),  # middle
    ("abc", "xxxxbca", True),  # end
    ("abc", "xxxxacb", True),  # end (another perm)

    # all chars not in s1 (reset-heavy)
    ("abc", "dddddddd", False),
    ("z", "aaaaaaaa", False),

    # windows with extra valid chars (should fail)
    ("ab", "aab", False),  # no length-2 window is "ab" or "ba"
    ("ab", "bbaa", False),

    # tricky mixes / classic
    ("adc", "dcda", True),
    ("hello", "ooolleoooleh", False),
    ("xyz", "afdgzyxksldfm", True),

    # many repeats in s2
    ("a", "aaaaaaaaaaaaaaa", True),
    ("bbb", "bbbbbbbb", True),
    ("bbb", "bbabb", False),

    # multiple resets + eventual match
    ("ab", "ccccccba", True),
    ("ab", "ccccccab", True),
    ("ab", "ccccccaa", False),

    # near-miss counts
    ("aabc", "abca", True),
    ("aabc", "abcc", False),

    # longer mixed
    ("abc", "cbaebabacd", True),
    ("abcd", "eidbacooo", False),
]

sol = Solution()

for i, (s1, s2, expected) in enumerate(tests, 1):
    result = sol.checkInclusion(s1, s2)
    print(f"Test {i}: s1={s1}, s2={s2}")
    print("Expected:", expected)
    print("Got     :", result)
    print("Correct :", result == expected)
    print("-" * 40)
