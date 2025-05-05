package src.Arrays.Easy;

public class Easy_121 {


    public int maxProfit(int[] prices) {
        int left = 0;

        int right = 1;
        int profit = 0;

        boolean t = false;
        while (left != right && left < prices.length && right < prices.length) {
            int diff = prices[right] - prices[left];
            if (diff > 0) {
                profit = Math.max(profit, diff);
            } else {
                left = right;
            }
            right++;


        }
        return profit;

    }

    public static void main(String[] args) {

        Easy_121 obj = new Easy_121();
        int[] prices = {7,1,5,3,6,4};
        System.out.println(obj.maxProfit(prices));
    }
}
