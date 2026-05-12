/*
*
*

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
*  well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

*
* */


package src.Strings.Medium;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution_22 {


    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            }
            else {
                if (stack.isEmpty()) {
                    return false;
                }

                char top = stack.pop();
                if ((c == ')' && top != '(')) {
                    return false;
                }
            }
        }

        // If the stack is empty, all brackets were matched correctly
        return stack.isEmpty();
    }

    public void generate(int n, List<String> res, String s, String[] brackets) {

        if (s.length() == (n * 2)) {
            if (isValid(s)) res.add(s);
            return;
        }

        for (String p : brackets) {
            s = s + p;
            generate(n, res, s, brackets);
            s = s.substring(0, s.length() - 1);
        }
    }

    public List<String> generateParenthesis(int n) {

        String s = "";
        List<String> res = new ArrayList<>();
        String[] brackets = new String[]{"(", ")"};
        generate(n, res, s, brackets);
        System.out.println(res);
        return res;
    }

    public static void main(String[] args) {
        int n = 3;
        Solution_22 obj = new Solution_22();
        obj.generateParenthesis(n);

    }
}
