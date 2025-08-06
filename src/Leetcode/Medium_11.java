package src.Arrays.Medium;

import static java.lang.Math.min;

class Medium_11 {
    public int maxArea(int[] height) {

        int max_area = 0;
        int right = height.length - 1;
        int left = 0;

        while (left < right) {
            int e_left = height[left];
            int e_right = height[right];
            int breadth = right - left;

            int length = min(e_left, e_right);
            int area = breadth * length;
            if (area > max_area) max_area = area;

            if (e_right > e_left) {
                left++;
            } else if (e_left > e_right) {
                right--;
            } else right--;
        }
        return (max_area);

    }

    public static void main(String[] args) {
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        Medium_11 obj = new Medium_11();
        System.out.println(obj.maxArea(height));
    }
}