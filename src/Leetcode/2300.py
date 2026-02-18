'''

2300. Successful Pairs of Spells and Potions

You are given two positive integer arrays spells and potions, of length n and m respectively,
where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful
if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.



Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
Thus, [2,0,2] is returned.

'''

from typing import List
import math


class Solution:

    def findMinTarget(self, potions, target) -> int:

        left = 0
        right = len(potions)-1
        res =0

        while left <= right:
            mid = (left + right) // 2

            if potions[mid] >= target :
                res = max(res, (len(potions)-1)-mid+1)
                right = mid - 1
            else:
                left = mid + 1

        return res

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()

        for spell in spells:
            target = math.ceil(success / spell)
            ans = self.findMinTarget(potions, target)
            res.append(ans)
        return res
# ----- Expected (brute force oracle) -----
def expected_successful_pairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    out = []
    for s in spells:
        cnt = 0
        for p in potions:
            if s * p >= success:
                cnt += 1
        out.append(cnt)
    return out


# ----- Edge + tricky test cases -----
tests = [
    # Provided example
    ("given_example", [3, 1, 2], [8, 5, 8], 16),

    # Minimal sizes
    ("single_single_success", [1], [1], 1),         # 1*1 >= 1 -> [1]
    ("single_single_fail", [1], [1], 2),            # 1*1 < 2 -> [0]

    # Duplicates everywhere
    ("all_duplicates", [2, 2, 2], [3, 3, 3, 3], 6), # 2*3 >= 6 -> [4,4,4]
    ("dups_mixed", [1, 2, 3], [1, 2, 2, 3, 3], 4),  # counts vary

    # Unsorted inputs (potions sorted inside)
    ("unsorted_potions", [4, 2], [5, 1, 10, 2], 20),  # targets: 5,10

    # Success very small / very large
    ("success_is_1", [1, 2, 100], [1, 2, 3], 1),       # always all potions
    ("huge_success", [1, 2, 3], [1, 2, 3, 10], 10**9), # likely all zeros

    # Threshold boundaries (ceil behavior)
    ("ceil_boundary_exact", [4], [5, 6, 7], 20),       # target=5 -> 3
    ("ceil_boundary_roundup", [3], [6, 7, 8], 20),     # target=7 -> 2

    # Mix that forces 0 and all
    ("mix_zero_and_all", [1, 10], [1, 2, 3, 4], 5),    # spell=1 => target=5 ->0 ; spell=10 => target=1 ->4

    # Large values (still safe in Python)
    ("large_values", [10**9, 10**9 - 1], [10**9, 2, 3], 10**18),

    # Many potions, varying spells
    ("varied", [5, 1, 7, 2], [1, 2, 3, 4, 5, 6], 15),

    # Empty edge cases (not typical LeetCode constraints, but good robustness checks)
    ("empty_spells", [], [1, 2, 3], 5),
    ("empty_potions", [1, 2, 3], [], 5),
]

sol = Solution()

passed = 0
failed = 0
failures = []

for name, spells, potions, success in tests:
    got = sol.successfulPairs(spells[:], potions[:], success)  # copy to avoid mutation effects
    exp = expected_successful_pairs(spells, potions, success)
    ok = got == exp
    if ok:
        passed += 1
    else:
        failed += 1
        failures.append((name, spells, potions, success, exp, got))

print(f"Total tests: {len(tests)} | Passed: {passed} | Failed: {failed}")
if failures:
    print("\nFAILED CASES:")
    for name, spells, potions, success, exp, got in failures:
        print("-" * 60)
        print("name   :", name)
        print("spells :", spells)
        print("potions:", potions)
        print("success:", success)
        print("expect :", exp)
        print("got    :", got)
else:
    print("All tests passed ✅")

spells = [3,1,2]
potions = [8,5,8]
success = 16
sol = Solution()
print(sol.successfulPairs(spells, potions, success))
