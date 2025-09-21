'''

187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences
(substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
'''

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        seqset = set()
        resset = set()
        for idx in range(len(s)-9):
            substr = s[idx:idx + 10]
            if substr in seqset:
                resset.add(substr)
            seqset.add(substr)
        return list(resset)


sol = Solution()
s = "AAAAAAAAAAA"
print(len(s))
print(sol.findRepeatedDnaSequences(s))
