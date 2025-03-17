package src.Strings.Medium;

import src.Arrays.Medium.Medium_1423;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

/*
* Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
* */
public class Medium_3 {

    public void println(Object s) {
        System.out.println(s);
    }

    public int lengthOfLongestSubstring(String s) {

        int left = 0;
        HashSet<Character> ui = new HashSet<>();
        int max = 0;
        for (int right = 0; right < s.length(); right++) {

            while (ui.contains(s.charAt(right))) {
                ui.remove(s.charAt(left));
                left++;
            }
            ui.add(s.charAt(right));

            max = Math.max(max, right-left+1);

        }

        return (max);
    }

    public static void main(String[] args) {
        String s = "pwwkew";
        Medium_3 obj = new Medium_3();
        System.out.println(obj.lengthOfLongestSubstring(s));
    }
}
