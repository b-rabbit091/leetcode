package src.Arrays.TwoPointer.Medium;

/*
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 */
public class Medium_5 {

    public String checkPalindrome(String s, int left, int right) {

        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return s.substring(left + 1, right);
    }

    public String longestPalindrome(String s) {
        String res = "";

        for (int i = 0; i < s.length(); i++) {
            String odd = checkPalindrome(s, i, i);
            String even = checkPalindrome(s, i, i + 1);
            String current_res = even.length() > odd.length() ? even : odd;

            if (current_res.length() > res.length()) {
                res = current_res;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        String s = "acbbcd";
        Medium_5 obj = new Medium_5();
        System.out.println(obj.longestPalindrome(s));


    }
}
