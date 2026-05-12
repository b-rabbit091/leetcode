/*
* Permutations
Solved
Medium
Topics
premium lock icon
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
*
* */


package src.Strings.Medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution_46 {

    public void generatePermutation(List<List<Integer>> res, int[] nums, int ind) {

        if (ind == nums.length) {
            ArrayList<Integer> temp = new ArrayList<>();
            for (int val : nums) temp.add(val);
            res.add(new ArrayList<>(temp));
            return;
        }

        for (int i = ind; i < nums.length; i++) {
            System.out.println(i +"  " + ind);;
            int temp = nums[i];
            nums[i] = nums[ind];
            nums[ind] = temp;

            generatePermutation(res, nums, ind + 1);

            temp = nums[i];
            nums[i] = nums[ind];
            nums[ind] = temp;
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        generatePermutation(res, nums, 0);
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        Solution_46 obj = new Solution_46();
        System.out.println(obj.permute(nums));
    }
}