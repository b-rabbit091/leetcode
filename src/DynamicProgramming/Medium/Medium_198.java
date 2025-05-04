package src.DynamicProgramming.Medium;

import java.util.Arrays;

/*
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
* */
public class Medium_198 {

    public long solution(int[] houses, int house_number, long[] memo) {
        if (houses.length == 1) {
            memo[house_number] = houses[0];
            return houses[0];
        } else if (house_number >= houses.length) return 0;
        else if (memo[house_number] != -1) return memo[house_number];

        long maxi = 0;
        for (int i = 2; i <= houses.length; i++) {
            long profit = houses[house_number] + solution(houses, house_number + i, memo);
            maxi = Math.max(maxi, profit);
        }
        memo[house_number] = maxi;
        return maxi;
    }

    public int rob(int[] nums) {
        long[] memo = new long[nums.length];
        Arrays.fill(memo, -1);
        for (int i = 0; i < nums.length; i++)
            solution(nums, i, memo);
        long max = memo[0];

        for (int i = 1; i < memo.length; i++) {
            if (memo[i] > max) {
                max = memo[i];
            }
        }
        return (int) max;

    }

    public static void main(String[] args) {
        int[] houses = {0};
        Medium_198 obj = new Medium_198();
        System.out.println(obj.rob(houses));

    }
}


