'''

554. Brick Wall

There is a rectangular brick wall in front of you with n rows of bricks.
The ith row has some number of bricks each of the same height (i.e., one unit)
but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks.
 If your line goes through the edge of a brick, then the brick is not considered as crossed.
 You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall,
return the minimum number of crossed bricks after drawing such a vertical line.

Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2
'''

from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        mp = {}
        mx = 0
        ln = len(wall)
        if ln == 0:
            return 0
        for i in wall:
            prev_value = 0
            for value in i[:-1]:
                current_sum = value + prev_value
                mp[current_sum] = mp.get(current_sum, 0) + 1
                prev_value += value
                mx = max(mx, mp.get(current_sum, 0))
        return ln - mx


sol = Solution()
wall = [[100000000], [100000000], [100000000]]
print(sol.leastBricks(wall))
