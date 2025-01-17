package src.Arrays.Medium;

/*

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
 */
public class Medium_33 {

    public int search(int[] nums, int target) {


        int start = 0;
        int end = nums.length - 1;
        int mid = 0;
        while (start <= end) {

            mid = (start + end) / 2;
            if (nums[mid] == target) return mid;

            if (nums[mid] >= nums[start]) {
                if (target <= nums[mid] && target >= nums[start]) {
                    end = mid - 1;
                } else start = mid + 1;
            } else if (nums[mid] <= nums[start]) {
                if (target >= nums[mid] && target <= nums[end]) {
                    start = mid + 1;
                } else end = mid - 1;

            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {7, 0, 1, 2, 3, 4, 5, 6};
        Medium_33 m = new Medium_33();
        System.out.println(m.search(nums, 6));

    }
}