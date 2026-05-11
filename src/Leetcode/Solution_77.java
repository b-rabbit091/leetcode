/*
*
77. Combinations
Medium
Topics
premium lock icon
Companies
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

*
* */


package src.Strings.Medium;

import java.util.ArrayList;
import java.util.List;

public class Solution_77 {
    public void generatePermutation(ArrayList<Integer> curr, List<List<Integer>> res, int n, int ind, int k) {
        if (curr.size() == k) {
            res.add(new ArrayList<>(curr));
            return;
        } else if (curr.size() > k) return;

        for (int i = ind; i <= n; i++) {
            curr.add(i);
            generatePermutation(curr, res, n, i + 1, k);
            curr.removeLast();
        }
    }
    public List<List<Integer>> combine(int n, int k) {

        ArrayList<Integer> curr = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        generatePermutation(curr, res, n, 1, k);
        return res;
    }
    public static void main(String[] z) {
        int n = 1;
        int k = 1;
        Solution_77 obj = new Solution_77();
        System.out.println(obj.combine(n, k));
    }
}
