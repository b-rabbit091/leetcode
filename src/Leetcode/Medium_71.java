package src.Strings.Medium;

import java.util.Stack;

public class Medium_71 {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        for (String s : path.split("/", -1)) {
            if (s.equals("..") ) {
                if( !stack.isEmpty())
                    stack.pop();

            } else if (s.equals(".") || s.isEmpty()) {
                continue;
            } else stack.push(s);
        }
        return "/"+String.join("/", stack);
    }

    public static void main(String[] args) {

        String path = "/..";
        Medium_71 obj = new Medium_71();
        System.out.println(obj.simplifyPath(path));

    }
}
