package src.Arrays.Medium;

import java.util.*;

public class Medium_18 {
    HashSet<List<Integer>> final_result = new HashSet<>();

    public boolean solution(int[] nums, int target, int index, long sum, ArrayList<Integer> result, int count) {

        if (count != 2) {

            for (int i = index; i < nums.length; i++) {
                result.add(nums[i]);
                sum = sum + nums[i];
                if (solution(nums, target, i + 1, sum, result, count + 1)) {
                    int left = i + 1;
                    int right = nums.length - 1;
                    while (left < right) {
                        long c = sum + nums[left] + nums[right];
                        if (c == target) {
                            Collections.addAll(result, nums[left], nums[right]);
                            Collections.sort(result);
                            final_result.add(new ArrayList<>(result));
                            result.remove((Integer) nums[left]);
                            result.remove((Integer) nums[right]);
                            right--;
                            left++;
                        } else if (c > target) {
                            right--;
                        } else left++;
                    }
                }
                sum = sum - nums[i];
                result.remove((Integer) nums[i]);
            }
        } else return true;
        return false;
    }

    public List<List<Integer>> fourSum(int[] nums, int target) {
        ArrayList<Integer> result = new ArrayList<>();
        Arrays.sort(nums);
        solution(nums, target, 0, 0, result, 0);
        return new ArrayList<>(final_result);
    }

    public static void main(String[] args) {
        int[] nums = {-3, -2, -1, 0, 0, 1, 2, 3};
        int target = 0;
        //int[] nums = {1000000000, 1000000000, 1000000000, 1000000000};
        //int target = -294967296;


        Medium_18 obj = new Medium_18();
        System.out.println(obj.fourSum(nums, target));
    }
}
