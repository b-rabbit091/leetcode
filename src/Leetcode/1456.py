'''
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.



'''


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = 0
        sumi = 0
        maxi = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        while right < len(s):

            while right - left + 1 <= k:
                if s[right] in vowels:
                    sumi += 1
                right += 1

            maxi = max(maxi, sumi)
            if s[left] in vowels:
                sumi -= 1
            left += 1
        return maxi


sol = Solution()
s = "abciiidef"
k = 3
print(sol.maxVowels(s, k))

# Test cases for Leetcode 1456: Maximum Number of Vowels in a Substring of Given Length

tests = [
    # Given examples
    ("abciiidef", 3, 3),
    ("aeiou", 2, 2),
    ("leetcode", 3, 2),

    # Edge cases
    ("a", 1, 1),  # smallest input, vowel
    ("b", 1, 0),  # smallest input, consonant
    ("aaaaa", 5, 5),  # all vowels, k = len(s)
    ("bcdfg", 5, 0),  # no vowels, k = len(s)

    # k = 1 cases
    ("abcde", 1, 1),  # single vowel max
    ("bbbbbb", 1, 0),  # no vowels at all

    # Mixed patterns
    ("abababab", 2, 1),  # alternating vowel/consonant
    ("aeaeaeae", 3, 3),  # repeating vowels
    ("zzzaeiouzzz", 5, 5),  # full vowel block inside

    # Large vowel streak at end
    ("bbbbbaeiou", 3, 3),
    ("bbbbbaeiou", 5, 5),

    # Large vowel streak at start
    ("aeioubbbb", 3, 3),
    ("aeioubbbb", 5, 5),

    # Random scenario
    ("thequickbrownfox", 4, 2),

    # All consonants except one vowel
    ("bbbbabbbb", 3, 1),

    # k in middle
    ("mississippi", 4, 2),
]

sol = Solution()

for i, (s, k, expected) in enumerate(tests, 1):
    result = sol.maxVowels(s, k)
    print(f"Test {i}: s={s}, k={k}")
    print("Expected:", expected)
    print("Got     :", result)
    print("Correct :", result == expected)
    print("-" * 50)
