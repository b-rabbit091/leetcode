package src.Arrays.Easy;

import java.util.Arrays;

/*
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 2,
with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 */
public class Easy_26 {
    public int removeDuplicates(int[] nums) {

        int index = 0;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if(max<nums[i]){
                max = nums[i];
                nums[index]=nums[i];
                index++;
            }
        }
        return index;
    }

    public static void main(String[] args) {
        //int[] nums = {0,0,1,1,1,2,2,3,3,4};
        int[] nums = {-3, -1, 0, 0};
        Easy_26 obj = new Easy_26();
        System.out.println(obj.removeDuplicates(nums));
        System.out.println(Arrays.toString(nums));
    }
}
