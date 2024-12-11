package src.Arrays;

import java.util.*;

/*
*
* Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Ex
*
* */
public class Medium_15 {
    public List<List<Integer>> threeSum(int[] nums) {

        ArrayList<Integer> result = new ArrayList<>();
        HashSet<List<Integer>> final_results = new HashSet<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {

            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int index_middle = i + 1;
            int index_right = nums.length - 1;
            int element_left = nums[i];

            while (index_middle < index_right && index_right < nums.length) {
                int element_middle = nums[index_middle];
                int element_right = nums[index_right];

                int sum = element_left + element_middle + element_right;

                if (sum == 0) {
                    Collections.addAll(result, element_left, element_middle, element_right);
                    Collections.sort(result);
                    final_results.add(new ArrayList<>(result));
                    result.clear();
                    index_middle++;
                    index_right--;
                } else if (sum > 0) index_right--;
                else {
                    index_middle++;
                }
            }
        }
        return new ArrayList<>(final_results);
    }

    public static void main(String[] args) {
        //int[] nums = {-1, 0, 1, 2, -1, -4};
        //int[] nums = {-3, 3, 4, -3, 1, 2};
        int[] nums = {-2, 0, 0, 2, 2};
        Medium_15 obj = new Medium_15();
        System.out.println(obj.threeSum(nums));
    }
}
