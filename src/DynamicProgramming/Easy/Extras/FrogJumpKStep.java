package src.DynamicProgramming.Easy.Extras;

import java.util.Arrays;


public class FrogJumpKStep {

    long solution(int[] arr, int index, long[] memo, int k) {

        if (index >= arr.length - 1) return 0;

        if (memo[index] != -1) return memo[index];
        long min = Integer.MAX_VALUE;


        for (int i = 1; i <= k; i++) {
            long cost = index + i >= arr.length ? Integer.MAX_VALUE : Math.abs(arr[index] - arr[index + i]) + solution(arr, index + i, memo, k);
            min = Math.min(min, cost);

        }
        memo[index] = min;
        return memo[index];

    }

    public static void main(String[] args) {
        FrogJumpKStep obj = new FrogJumpKStep();
        int[] arr = {50, 90, 80, 10, 20};
        long[] memo = new long[arr.length + 1];
        Arrays.fill(memo, -1);
        int jump = 2;
        System.out.println(obj.solution(arr, 0, memo, jump));

    }
}
