/*
 71. Simplify Path

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.
For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.


 */


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
