package src.Arrays.Medium;


/*
* Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
* */
public class Medium_1423 {


    public int maxScore(int[] cardPoints, int k) {

        int sum = 0;
        for (int i = 0; i < k; i++)
            sum = sum + cardPoints[i];

        int max = sum;

        for (int j = 0; j < k; j++) {
            int right =cardPoints.length - j - 1;
            int left = k - j - 1;
            max = max + cardPoints[right] - cardPoints[left];
            if (max > sum) sum = max;
        }

        return sum;
    }

    public static void main(String[] args) {

        int[] arr = {2, 2, 2};
        int k = 2;
        Medium_1423 obj = new Medium_1423();
        System.out.println(obj.maxScore(arr, k));


    }
}
