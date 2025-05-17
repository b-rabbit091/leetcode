class Solution:

    def calc_curr_sum(self, first_char, second_char, mp):
        clockwise = abs(mp[first_char] - mp[second_char])
        anti_clockwise = (26- max(mp[second_char] , mp[first_char]) + min(mp[second_char] , mp[first_char]) )
        return min(clockwise, anti_clockwise) + 1

    def minTimeToType(self, word: str) -> int:
        curr_sum = 0
        mp = dict()

        for i in range(1, 27):
            mp[chr(96 + i)] = i
        length = len(word)

        if word[0] == 'a':
            curr_sum = 1
        else:
            first_char = 'a'
            second_char = word[0]
            curr_sum = curr_sum + self.calc_curr_sum(first_char, second_char, mp)

        for i in range(length - 1):
            first_char = word[i]
            second_char = word[i + 1]
            curr_sum = curr_sum + self.calc_curr_sum(first_char, second_char, mp)
        return curr_sum


sol = Solution()
s = "abc"
print(sol.minTimeToType(s))
