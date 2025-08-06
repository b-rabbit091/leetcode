package src.Arrays.Medium;

import java.util.HashMap;
import java.util.HashSet;

public class Medium_36 {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, HashSet<Character>> row = new HashMap<>();
        HashMap<Integer, HashSet<Character>> col = new HashMap<>();
        HashMap<String, HashSet<Character>> square = new HashMap<>();


        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                char element = board[i][j];
                if (!(element == '.')) {
                    String key = (i / 3) + "-" + (j / 3);

                    if (row.getOrDefault(i, new HashSet<>()).contains(element) || col.getOrDefault(j, new HashSet<>()).contains(element) || square.getOrDefault(key, new HashSet<>()).contains(element)) {
                        return false;
                    } else {
                        row.putIfAbsent(i, new HashSet<>());
                        row.get(i).add(element);

                        col.putIfAbsent(j, new HashSet<>());
                        col.get(j).add(element);

                        square.putIfAbsent(key, new HashSet<>());
                        square.get(key).add(element);

                    }
                }

            }

        }
        return true;

    }


    public static void main(String[] args) {
        char[][] board = {{'5', '3', '.', '.', '7', '.', '.', '.', '.'}, {'5', '.', '.', '1', '9', '5', '.', '.', '.'}, {'.', '9', '8', '.', '.', '.', '.', '6', '.'}, {'8', '.', '.', '.', '6', '.', '.', '.', '3'}, {'4', '.', '.', '8', '.', '3', '.', '.', '1'}, {'7', '.', '.', '.', '2', '.', '.', '.', '6'}, {'.', '6', '.', '.', '.', '.', '2', '8', '.'}, {'.', '.', '.', '4', '1', '9', '.', '.', '5'}, {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};
        Medium_36 obj = new Medium_36();
        System.out.println(obj.isValidSudoku(board));

    }
}