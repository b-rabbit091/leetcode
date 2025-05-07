'''
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen
numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
 Two combinations are unique if the frequency of at least one of the chosen
 numbers is different.

The test cases are generated such that the number of unique combinations that sum up to
target is less than 150 combinations for the given input.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.


Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

'''

from typing import List


class Solution:

    def recursionSolution(self, candidates, target, res, fin, index):

        if target == 0:
            fin.add(tuple(res.copy()))
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            if i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                continue
            if target - candidates[i] >= 0:
                res.append(candidates[i])
                self.recursionSolution(candidates, target - candidates[i], res, fin, i + 1)

                res.pop()

        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        fin = set()
        index = 0
        candidates.sort()
        if sum(candidates) == target:
            return [candidates]
        self.recursionSolution(candidates, target, res, fin, index)
        result = [list(t) for t in fin]

        return result


sol = Solution()
candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
target = 30
print(sol.combinationSum2(candidates, target))
