package src.DynamicProgramming.Easy.Extras;

import java.util.Arrays;


/*
* Input: heights[] = [20, 30, 40, 20]
Output: 20
Explanation:  Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
jump from stair 0 to 1: cost = |30 - 20| = 10
jump from stair 1 to 3: cost = |20-30|  = 10
Total Cost = 10 + 10 = 20

* 20
* 30, 40
* 30 - > 40 , 20
* 40 -> 20
* 20 = 20
*
*
*
Input: heights[] = [30, 20, 50]
Output: 30
Explanation: Minimum cost will be incurred when frog jumps from stair 0 to 2 then 2 to 4:
jump from stair 0 to 2: cost = |50 - 30| = 20
jump from stair 2 to 4: cost = |40-50|  = 10
Total Cost = 20 + 10 = 30
* */
public class FrogJump {

    long solution(int[] arr, int index, long[] memo) {

        if (index >= arr.length - 1) return 0;

        if (memo[index] != -1) return memo[index];

        long cost1 = index + 1 >= arr.length ? Integer.MAX_VALUE :
                Math.abs(arr[index] - arr[index + 1]) + solution(arr, index + 1, memo);

        long cost2 = index + 2 >= arr.length ? Integer.MAX_VALUE :
                Math.abs(arr[index] - arr[index + 2]) + solution(arr, index + 2, memo);

        memo[index] = Math.min(cost1, cost2);

        return memo[index];
    }

    public static void main(String[] args) {
        FrogJump obj = new FrogJump();
        int[] arr = {20, 30, 40, 20, 40, 80, 10};
        long[] memo = new long[arr.length + 1];
        Arrays.fill(memo, -1);
        System.out.println(obj.solution(arr, 0,  memo));

    }
}
