package src.Arrays.Easy;

import java.util.Arrays;

/*
* Input: nums = [2,2,3,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
*
* */
public class Easy_27 {
    public int removeElement(int[] nums, int val) {
        int index = 0;
        int left = 0;
        while (left < nums.length && index < nums.length) {

            if (nums[index] != val) {
                index++;
            } else if (nums[index] == val && nums[left] != val) {
                int temp = nums[index];
                nums[index] = nums[left];
                nums[left] = temp;
                index++;
            }
            left++;
        }
        return index;
    }

    public static void main(String[] args) {

        int[] nums = {3, 0, 1, 2, 2, 3, 0, 4, 2, 3};
        int val = 3;
        Easy_27 obj = new Easy_27();
        System.out.println(obj.removeElement(nums, val));
        System.out.println(Arrays.toString(nums));
    }
}
