from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        curr_sum = 0

        seats = sorted(seats)
        students = sorted(students)
        min_ind = min(len(seats), len(students))
        for i in range(min_ind):
            sd = students[i]
            st = seats[i]
            curr_sum = curr_sum + abs(sd - st)

        return curr_sum


sol = Solution()
print(sol.minMovesToSeat(seats = [4,1,5,9], students = [1,3,2,6]))
