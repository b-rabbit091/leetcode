
class Solution:

    def generateTiles(self, tiles, temp_list, res, ind, s):

        if ind > len(tiles):
            return
        elif len(s) > 0:
            res.add(s)

        for i in range(ind, len(tiles)):
            temp_list[i], temp_list[ind] = temp_list[ind], temp_list[i]
            s = "".join(temp_list[:ind + 1])
            self.generateTiles(tiles, temp_list, res, ind + 1, s)
            temp_list[i], temp_list[ind] = temp_list[ind], temp_list[i]


    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        temp_list = list(tiles)
        self.generateTiles(tiles, temp_list, res, 0, '')
        return len(res)


obj = Solution()
tiles = "AAABBC"
print(obj.numTilePossibilities(tiles))
