package src.DynamicProgramming.Easy;

import java.util.Arrays;

public class Easy_1137 {

    static int calcTrib(int[] dp, int index) {

        if (index == 0) {
            return 0;
        } else if (index == 1 || index == 2) {
            return 1;
        }
        if (dp[index] != -1) return dp[index];

        dp[index] = calcTrib(dp, index - 1) + calcTrib(dp, index - 2) + calcTrib(dp, index - 3);
        return dp[index];

    }

    static void printTrib(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        int resul = calcTrib(dp, n);
        System.out.println(resul);

    }


    public static void main(String[] args) {
        int n = 25;
        printTrib(n);

    }
}
