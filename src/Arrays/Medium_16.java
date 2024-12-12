package src.Arrays;

import java.util.*;

/*
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


 */
public class Medium_16 {
    public int threeSumClosest(int[] nums, int target) {

        Arrays.sort(nums);
        int nearest_element_distance = Integer.MAX_VALUE;
        int nearest_element = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int index_middle = i + 1;
            int index_right = nums.length - 1;
            int element_left = nums[i];

            while (index_middle < index_right && index_right < nums.length) {
                int element_middle = nums[index_middle];
                int element_right = nums[index_right];
                int sum = element_left + element_middle + element_right;

                if (sum < target) {
                    index_middle++;
                } else index_right--;

                int distance = sum - target;
                distance = distance < 0 ? -distance : distance;
                if (distance < nearest_element_distance) {
                    nearest_element_distance = distance;
                    nearest_element = sum;
                }
            }
        }
        return nearest_element;
    }

    public static void main(String[] args) {
        int[] nums = {1, 1, 1, 0};
        int target = -100;
        Medium_16 obj = new Medium_16();
        System.out.println(obj.threeSumClosest(nums, target));
    }
}
