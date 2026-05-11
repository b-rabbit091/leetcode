package src.Strings.Medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/*
*
40. Combination Sum II
Solved
Medium
Topics
premium lock icon
Companies
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

*
* */
public class Solution_40 {
    public void generateCombinationAndSum(int[] candidates, ArrayList<Integer> curr, List<List<Integer>> res, int sum, int target, int ind) {
        if (sum == target) {
            ArrayList<Integer> temp = new ArrayList<>(curr);
            res.add(temp);
            return;
        } else if (sum > target) return;

        for (int i = ind; i < candidates.length; i++) {
            if (i > ind && candidates[i] == candidates[i - 1]) {
                continue;
            }
            curr.add(candidates[i]);
            sum += candidates[i];
            generateCombinationAndSum(candidates, curr, res, sum, target, i + 1);
            sum -= candidates[i];
            curr.removeLast();
        }
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {

        ArrayList<Integer> curr = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        generateCombinationAndSum(candidates, curr, res, 0, target, 0);
        return res;
    }

    public static void main(String[] args) {
        int[] candidates = {2, 5, 2, 1, 2};
        int target = 5;
        Solution_40 obj = new Solution_40();
        System.out.println(obj.combinationSum2(candidates, target));

    }
}
