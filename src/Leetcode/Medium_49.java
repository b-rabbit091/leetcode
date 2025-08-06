package src.Strings.Medium;


/*
* 49. Group Anagrams

Given an array of strings strs, group the anagrams together.
* You can return the answer in any order.
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
* */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Medium_49 {

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> mp = new HashMap<>();
        for (String s : strs) {
            char[] tempStr = s.toCharArray();
            Arrays.sort(tempStr);
            String sortedStr = new String(tempStr);
            List<String> res = mp.get(sortedStr);

            if (!mp.containsKey(sortedStr)) {
                List<String> elem = new ArrayList<>();
                elem.add(s);
                mp.put(sortedStr, elem);
            } else {
                res.add(s);
                mp.put(sortedStr, res);
            }

        }

        return new ArrayList<>(mp.values());


    }

    public static void main(String[] args) {
        String[] strs = {"ddddddddddg", "dgggggggggg"};
        Medium_49 obj = new Medium_49();
        System.out.println(obj.groupAnagrams(strs));
    }
}