'''

1980. Find Unique Binary String

Given an array of strings nums containing n unique binary strings each of length n,
return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.


'''

from typing import List


class Solution:

    def solve(self, nums, ind, res):

        if len(res) == len(nums) and (res not in set(nums)):
            return res

        elif res in set(nums):
            return ''

        for i in ["0","1"]:
            res += i
            curr = self.solve(nums, ind + 1, res)
            if curr != '':
                return curr
            res = res[:-1]
        return ''

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ind, res = 0, ''
        curr = self.solve(nums, ind, res)
        return curr


sol = Solution()
nums = ["0"]
print(sol.findDifferentBinaryString(nums))

test_cases = [
    (["01", "10"], {"00", "11"}),

    (["00", "01"], {"10", "11"}),

    (["111", "011", "001"], {"000", "010", "100", "101", "110"}),

    (["000", "001", "010"], {"011", "100", "101", "110", "111"}),

    (["0"], {"1"}),

    (["1"], {"0"}),

    (["00", "10"], {"01", "11"}),

    (["10", "11"], {"00", "01"}),

    (["0000", "0001", "0010", "0011"], {
        "0100", "0101", "0110", "0111",
        "1000", "1001", "1010", "1011",
        "1100", "1101", "1110", "1111"
    }),

    (["1111", "1110", "1101", "1100"], {
        "0000", "0001", "0010", "0011",
        "0100", "0101", "0110", "0111",
        "1000", "1001", "1010", "1011"
    }),
]


sol = Solution()

for i, (nums, valid_outputs) in enumerate(test_cases, 1):
    output = sol.findDifferentBinaryString(nums)

    if output in valid_outputs and output not in nums and len(output) == len(nums[0]):
        print(f"Test {i}: RIGHT | nums={nums} | output={output}")
    else:
        print(f"Test {i}: WRONG | nums={nums}")
        print(f"  Your output: {output}")
        print(f"  Valid outputs: {valid_outputs}")
        print()