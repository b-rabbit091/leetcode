/*
* 120. Triangle
Medium
Topics
premium lock icon
Companies
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
* More formally, if you are on index i on the current row,
* you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
*
* */

package src.Strings.Medium;

import java.util.Arrays;
import java.util.List;

public class Solution_120 {

    public int solve(List<List<Integer>> triangle, int row, int ind, int[][] dp) {
        if (row >= triangle.size() || ind >= triangle.get(row).size()) return 0;
        else if (dp[row][ind] != Integer.MAX_VALUE) return dp[row][ind];
        int mini1 = triangle.get(row).get(ind) + solve(triangle, row + 1, ind, dp);
        int mini2 = triangle.get(row).get(ind) + solve(triangle, row + 1, ind + 1, dp);
        dp[row][ind] = Math.min(mini1, mini2);
        return dp[row][ind];
    }

    public int minimumTotal(List<List<Integer>> triangle) {

        if (triangle.size() == 1) return triangle.get(0).get(0);
        int[][] dp = new int[triangle.size()][triangle.size()];
        for (int[] row : dp) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        int sum1 = triangle.get(0).get(0) + solve(triangle, 1, 0, dp);
        int sum2 = triangle.get(0).get(0) + solve(triangle, 1, 1, dp);
        return Math.min(sum1, sum2);

    }

    public static void main(String[] args) {

        List<List<List<Integer>>> testCases = List.of(

                // Test 1: Single element
                List.of(
                        List.of(7)
                ),

                // Test 2: Two rows with negative numbers
                List.of(
                        List.of(1),
                        List.of(-2, -3)
                ),

                // Test 3: All zeroes
                List.of(
                        List.of(0),
                        List.of(0, 0),
                        List.of(0, 0, 0),
                        List.of(0, 0, 0, 0)
                ),

                // Test 4: Minimum path moves toward the middle
                List.of(
                        List.of(5),
                        List.of(1, 100),
                        List.of(100, 1, 100),
                        List.of(100, 100, 1, 100)
                ),

                // Test 5: Smallest immediate value is not always best
                List.of(
                        List.of(1),
                        List.of(2, 3),
                        List.of(100, 100, 1),
                        List.of(1, 1, 1, 1)
                ),

                // Test 6: All negative numbers
                List.of(
                        List.of(-1),
                        List.of(-2, -3),
                        List.of(-4, -5, -6),
                        List.of(-7, -8, -9, -10)
                ),

                // Test 7: Large positive and negative numbers
                List.of(
                        List.of(10),
                        List.of(100, -100),
                        List.of(100, 100, -100),
                        List.of(100, 100, 100, -100)
                ),

                // Test 8: Multiple paths have the same minimum
                List.of(
                        List.of(2),
                        List.of(1, 1),
                        List.of(1, 1, 1)
                ),

                // Test 9: Values near constraint boundaries
                List.of(
                        List.of(10000),
                        List.of(-10000, 10000),
                        List.of(-10000, -10000, 10000)
                ),

                // Test 10: Minimum path stays on the right side
                List.of(
                        List.of(1),
                        List.of(100, 2),
                        List.of(1, 100, 3),
                        List.of(1, 1, 100, 4)
                )
        );

        List<Integer> expectedResults = List.of(
                7,
                -2,
                0,
                8,
                6,
                -20,
                -290,
                4,
                -10000,
                10
        );

        Solution_120 solution = new Solution_120();

        int passed = 0;

        for (int i = 0; i < testCases.size(); i++) {
            List<List<Integer>> triangle = testCases.get(i);

            int expected = expectedResults.get(i);
            int actual = solution.minimumTotal(triangle);

            boolean isPassed = expected == actual;

            if (isPassed) {
                passed++;
            }

            System.out.println("Test Case " + (i + 1));
            System.out.println("Triangle : " + triangle);
            System.out.println("Expected : " + expected);
            System.out.println("Actual   : " + actual);
            System.out.println("Result   : " + (isPassed ? "PASS" : "FAIL"));
            System.out.println("----------------------------------");
        }

        System.out.println(
                "Passed " + passed + " out of " + testCases.size() + " tests."
        );
    }
}

