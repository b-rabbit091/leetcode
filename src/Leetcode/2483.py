'''
2483. Minimum Penalty for a Shop

You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.



Example 1:

Input: customers = "YYNY"
Output: 2
Explanation:
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.
Example 3:

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.

'''


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yes = []
        no = []
        y = 0
        n = 0
        for i in customers:
            if i == 'Y':
                y += 1
            elif i == 'N':
                n += 1
            yes.append(y)
            no.append(n)

        mini = 0
        hour = 0

        for idx in range(len(customers) + 1):
            past_penality = 0 if idx == 0 else no[idx - 1]
            future_penality = 0 if (idx or idx + 1) >= len(customers) else yes[-1] - (
                yes[idx - 1] if idx - 1 >= 0 else 0)
            total_penalty = past_penality + future_penality

            if idx == 0:
                mini = total_penalty

            if total_penalty < mini:
                hour = idx
                mini = total_penalty
        return hour


sol = Solution()
customers = "YYNY"
print(sol.bestClosingTime(customers))
