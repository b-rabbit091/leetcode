'''
1052. Grumpy Bookstore Owner

There is a bookstore owner that has a store open for n minutes.
You are given an integer array customers of length n where customers[i] is the number
of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

During certain minutes, the bookstore owner is grumpy.
You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

Return the maximum number of customers that can be satisfied throughout the day.


Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

Output: 16

Explanation:

The bookstore owner keeps themselves not grumpy for the last 3 minutes.

The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Example 2:

Input: customers = [1], grumpy = [0], minutes = 1

Output: 1

'''

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        start = 0
        end = 0
        i = 0
        maxi = 0
        t=0
        while (i + minutes) <= len(customers):
            res = 0
            for x in range(i, i + minutes):
                if grumpy[x] == 1:
                    res += customers[x]
            if res>t:
                t= res
                start=i
                end = i+minutes-1
            i+=1
        for idx1, val in enumerate(customers):
            if start <= idx1 <= end or grumpy[idx1] == 0:
                maxi += val
        return maxi


sol = Solution()
customers = [4, 10, 10]
grumpy = [1, 1, 0]
minutes = 2
print(sol.maxSatisfied(customers, grumpy, minutes))
# Each item: (customers, grumpy, minutes, expected_correct)
# All follow:
# 1 <= minutes <= n <= 2*10^4, 0<=customers[i]<=1000, grumpy[i] in {0,1}

test_cases = [
    # 1) smallest n
    ([1], [0], 1, 1),
    ([5], [1], 1, 5),

    # 2) minutes = 1
    ([2, 3, 4], [1, 0, 1], 1, 7),
    ([0, 0, 10], [1, 1, 1], 1, 10),

    # 3) minutes = n (should become sum(customers))
    ([4, 10, 2], [1, 1, 1], 3, 16),
    ([3, 0, 5, 1], [0, 1, 1, 0], 4, 9),

    # 4) mixed / classic
    ([1, 0, 1, 2, 1, 1, 7, 5],
     [0, 1, 0, 1, 0, 1, 0, 1],
     3,
     16),

    # 5) no grumpy
    ([3, 8, 2], [0, 0, 0], 2, 13),

    # 6) all grumpy
    ([4, 3, 2], [1, 1, 1], 2, 7),
    ([1000, 1000, 1000, 1000], [1, 1, 1, 1], 3, 3000),

    # 7) window best at start / middle / end
    ([9, 1, 1, 1, 1], [1, 0, 1, 1, 1], 2, 12),  # best window at end (adds 1+1)
    ([1, 2, 10, 2, 1], [1, 1, 1, 1, 1], 2, 12),  # best window includes 10
    ([5, 1, 1, 1, 5], [1, 0, 1, 0, 1], 1, 7),  # pick one of the 5's

    # 8) lots of zeros
    ([0, 0, 0, 7, 0], [1, 1, 1, 1, 1], 2, 7),
    ([0, 4, 0, 0, 4], [0, 1, 0, 1, 0], 2, 8),
]
for idx, (customers, grumpy, minutes, expected) in enumerate(test_cases, 1):
    got = sol.maxSatisfied(customers, grumpy, minutes)
    print(idx, got, expected, got == expected)
