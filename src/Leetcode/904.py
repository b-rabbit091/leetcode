'''
904. Fruit Into Baskets
Medium
Topics
premium lock icon
Companies
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit.
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree
(including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.



Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
'''
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        right = 0
        left = 0
        maxi = 0
        mp = {}

        while right < len(fruits):
            mp[fruits[right]] = mp.get(fruits[right], 0) + 1
            while len(mp) > 2:
                update_value = mp[fruits[left]] - 1
                if update_value <= 0:
                    del mp[fruits[left]]
                else:
                    mp[fruits[left]] = update_value
                left += 1
            maxi = max(maxi, right - left + 1)
            right += 1

        return maxi


sol = Solution()
fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(sol.totalFruit(fruits))

tests = [
    # Examples
    ([1, 2, 1], 3),
    ([0, 1, 2, 2], 3),
    ([1, 2, 3, 2, 2], 4),

    # Edge cases
    ([1], 1),
    ([1, 1, 1, 1], 4),
    ([1, 2], 2),
    ([1, 2, 3], 2),

    # All same fruit
    ([5, 5, 5, 5, 5], 5),

    # Exactly two fruit types
    ([1, 2, 1, 2, 1, 2], 6),

    # Switch fruit types frequently
    ([1, 2, 3, 1, 2, 3, 1], 2),

    # Long valid window in middle
    ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),

    # Best window at start
    ([1, 1, 2, 2, 3], 4),

    # Best window at end
    ([3, 1, 2, 2, 2], 4),

    # Complex case
    ([1, 0, 1, 4, 1, 4, 1, 2, 3], 5),

    # Large block then new fruit
    ([2, 2, 2, 2, 3, 3, 3, 1], 7),

    # Alternating then break
    ([1, 2, 1, 2, 1, 3, 3, 3, 3], 5),
]

sol = Solution()

for i, (fruits, expected) in enumerate(tests, 1):
    result = sol.totalFruit(fruits)
    print(f"Test {i}: fruits={fruits}")
    print("Expected:", expected)
    print("Got     :", result)
    print("Correct :", result == expected)
    print("-" * 50)
