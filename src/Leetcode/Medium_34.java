package src.Arrays.Medium;

import java.util.Arrays;

/*
*
Given an array of integers nums sorted in non-decreasing order,
* find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
* */
public class Medium_34 {
    public int[] searchRange(int[] nums, int target) {

        int left = 0;
        int right = nums.length - 1;
        int lindex = -1;
        int rindex = -1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                lindex = mid;
                rindex = mid;

                while (nums[lindex-1] == target) {
                    lindex--;
                }
                while (nums[rindex+1] == target) {
                    rindex++;
                }
                break;

            } else if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) right = mid - 1;
        }
        return new int[]{lindex, rindex};

    }

    public static void main(String[] args) {

        int[] nums = {6, 7, 8, 8, 8,8,8, 9, 10};
        Medium_34 obj = new Medium_34();
        System.out.println(Arrays.toString(obj.searchRange(nums, 8)));
    }
}
