package src.Strings.Medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Solution_47 {


    public void generatePermute(int[] nums, List<List<Integer>> res, int idx) {

        if (idx == nums.length) {
            ArrayList<Integer> curr = new ArrayList<>();
            for (int val : nums)
                curr.add(val);
            if (!(res.contains(curr)))
                res.add(curr);
            return;
        }

        for (int i = idx; i < nums.length; i++) {
            int temp = nums[i];
            nums[i] = nums[idx];
            nums[idx] = temp;

            generatePermute(nums, res, idx + 1);

            temp = nums[i];
            nums[i] = nums[idx];
            nums[idx] = temp;
        }

    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        generatePermute(nums, res, 0);
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        Solution_47 obj = new Solution_47();
        System.out.println(obj.permuteUnique(nums));
    }

}
