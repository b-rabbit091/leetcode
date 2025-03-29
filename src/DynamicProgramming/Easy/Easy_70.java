package src.DynamicProgramming.Easy;

import java.util.HashMap;
import java.util.List;

/*
* You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
*
* */
class Easy_70 {

    HashMap<Integer, Integer> mp = new HashMap<>();
    public int helper(int n, int init, int count) {

        if (init == n) {
            count = count + 1;
            return count;
        } else if (init > n) {
            return count;
        }

        if (mp.containsKey(init))
            return mp.get(init);
        int count1 = helper(n, init + 1, count);
        int count2 = helper(n, init + 2, count);
        mp.put(init, count1 + count2);
        return count1 + count2;
    }

    public int climbStairs(int n) {
        return (helper(n, 0, 0));
    }

    public static void main(String[] args) {
        int n = 5;
        Easy_70 obj = new Easy_70();
        System.out.println(obj.climbStairs(n));
    }
}
