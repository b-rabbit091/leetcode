package src.Arrays.Easy;

/*
*
* Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
* */
public class Easy_35 {

    public int searchInsert(int[] nums, int target) {

        int left = 0;
        int right = nums.length - 1;

        while (left < right) {

            int mid = (left + right) / 2;

            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            }
        }
        return nums[left] >= target ? left : left + 1;

    }

    public static void main(String[] args) {
        int[] nums = {1, 3, 5, 6, 8, 9, 10};
        int target = 7;
        Easy_35 obj = new Easy_35();
        System.out.println(obj.searchInsert(nums, target));
    }
}
