package src.Arrays.TwoPointer.Medium;

import java.util.Locale;

/*
*
* Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

* */
public class Medium_28 {

    public void println(String s) {
        System.out.println(s);
    }

    public int strStr(String haystack, String needle) {
        int l = needle.length();
        int min = -1;
        for (int i = 0; i < haystack.length(); i++) {
            for (int j = haystack.length(); (j - l) >= 0 && i + l <= haystack.length(); j--) {
                String first = haystack.substring(i, i + l);
                int second_index = j - (l);
                String second = haystack.substring(second_index, second_index + l);
                if (second.equals(needle) && first.equals(second)) {
                    return i;
                }
            }
        }
        return min;
    }

//    public int strStr(String haystack, String needle) {
//        for (int i = 0; i < haystack.length() - needle.length()+1; i++) {
//
//            if (haystack.substring(i, i + needle.length()).equals(needle))
//                return i;
//        }
//
//        return -1;
//    }

    public static void main(String[] args) {
        String haystack = "stdbutsad";
        String needle = "sad";
        Medium_28 obj = new Medium_28();
        System.out.println(obj.strStr(haystack, needle));

    }
}
