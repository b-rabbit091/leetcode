package src.Strings.Medium;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;

/*
* 2616. Minimize the Maximum Difference of Pairs

You are given a 0-indexed integer array nums and an integer p.
* Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized.
* Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|,
* where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.



Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5.
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
*
* */
public class Solution_2616 {
    public int minimizeMax(int[] nums, int p) {

        int left = 0;
        int right = Integer.MAX_VALUE;
        int mini = nums[nums.length-1]-nums[0];
        Arrays.sort(nums);
        while (left <= right) {

            int mid = left + (right - left) / 2;
            int count = 0;

            for (int i = 0; i < nums.length - 1; i++) {
                int diff = Math.abs(nums[i] - nums[i + 1]);
                if (diff <= mid) {
                    count += 1;
                    i=i+1;
                }
            }
            if (count >= p) {
                    mini = mid;
                right = mid - 1;
            }
            else left = mid + 1;
        }
        return mini;

    }

    public static void main(String[] z) {

        int[] nums = {10, 1, 2, 7, 1, 3};
        int p = 2;
        Solution_2616 obj = new Solution_2616();
        System.out.println(obj.minimizeMax(nums, p));


    }


}
