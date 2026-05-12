/*
*
90. Subsets II
Medium
Topics
premium lock icon
Companies
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
*
* */

package src.Strings.Medium;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution_90 {

    public void generateSubset(ArrayList<Integer> curr, List<List<Integer>> res, int ind, int[] nums) {

        if (ind > nums.length)
            return;


        res.add(new ArrayList<>(curr));

        for (int i = ind; i < nums.length; i++) {
            if (i > ind && nums[i] == nums[i - 1]) continue;
            curr.add(nums[i]);
            generateSubset(curr, res, i + 1, nums);
            curr.removeLast();
        }
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {

        ArrayList<Integer> curr = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        generateSubset(curr, res, 0, nums);
        return res;

    }

    public static void main(String[] args) {

        int[] nums = {1, 2, 2};
        Solution_90 obj = new Solution_90();
        System.out.println(obj.subsetsWithDup(nums));

    }
}
