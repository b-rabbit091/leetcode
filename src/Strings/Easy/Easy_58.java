package src.Strings.Easy;

public class Easy_58 {
    public int lengthOfLastWord(String s) {

        s = s.trim();
        for (int i = s.length() - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            if (ch == ' ') {
                return s.substring(i+1).length();
            }
        }

        return s.length();
    }

    public static void main(String[] args) {
        String s = "l";
        Easy_58 obj = new Easy_58();
        System.out.println(obj.lengthOfLastWord(s));

    }
}
