package src.Strings.Medium;

import java.util.ArrayList;
import java.util.List;

/*

78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
* */
public class Solution_78 {

    public void generateSubset(int[] nums, ArrayList<Integer> curr, List<List<Integer>> res, int ind) {

        res.add(new ArrayList<>(curr));
        for (int i = ind; i < nums.length; i++) {
            curr.add(nums[i]);
            generateSubset(nums, curr, res, i + 1);
            curr.removeLast();
        }
    }

    public List<List<Integer>> subsets(int[] nums) {

        ArrayList<Integer> curr = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        generateSubset(nums, curr, res, 0);
        return res;

    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        Solution_78 obj = new Solution_78();
        System.out.println(obj.subsets(nums));
    }
}
