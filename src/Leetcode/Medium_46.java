package src.Arrays.Medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Medium_46 {
     List<Integer> res = new ArrayList<>();
     List<List<Integer>> res2 = new ArrayList<>();

    public void generatePermutation(int[] n, int[] clone, int index) {

        if (res.size() == n.length) {
            res2.add(new ArrayList<>(res));
            return;
        }

        for (int i = index; i < n.length; i++) {
            res.add(n[i]);
            swap(i, index, n);
            generatePermutation(n, clone, index + 1);
            swap(i, index, n);
            res.remove((Integer) n[i]);
        }
    }

    public void swap(int i, int j, int[] n) {
        int temp = n[i];
        n[i] = n[j];
        n[j] = temp;
    }

    public List<List<Integer>> permutation(int[] nums) {
        int[] cloneNums = nums.clone();
        Arrays.sort(nums);
        generatePermutation(nums, cloneNums, 0);
        return res2;


    }

    public static void main(String[] args) {
        int[] nums = {1};
        Medium_46 obj = new Medium_46();
        System.out.print( obj.permutation(nums));
        //System.out.println(Arrays.toString(nums));
    }
}
