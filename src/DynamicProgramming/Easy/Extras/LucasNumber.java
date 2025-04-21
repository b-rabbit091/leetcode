package src.DynamicProgramming.Easy.Extras;

import java.util.Arrays;

/*
Lucas numbers are similar to Fibonacci numbers.
Lucas numbers are also defined as the sum of its two immediately previous terms.
But here the first two terms are 2 and 1 whereas in Fibonacci numbers the first two
terms are 0 and 1 respectively.

Input : 3
Output : 4

Input : 7
Output : 29

 */
public class LucasNumber {

    static int lucas(int[] dp, int n) {
        if (n == 0)
            return 2;
        else if (n == 1) return 1;
        if (dp[n] != -1) return dp[n];
        dp[n] = lucas(dp, n - 1) + lucas(dp, n - 2);
        return dp[n];
    }

    static int prepDp(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return lucas(dp, n);
    }

    public static void main(String[] args) {
        int n = 9;
        System.out.println(prepDp(n));
    }
}
