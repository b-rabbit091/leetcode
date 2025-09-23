'''
1461. Check If a String Contains All Binary Codes of Size K

Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.



Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
Example 3:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.


'''

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique_binary_sets = pow(2, k)
        unique_codes = set()
        for i in range(0, len(s)):
            if i + k > len(s):
                continue
            else:
                code = s[i:i + k]
                unique_codes.add(code)
        return len(unique_codes) == unique_binary_sets


sol = Solution()
s = "0110"
k = 1
print(sol.hasAllCodes(s, k))
