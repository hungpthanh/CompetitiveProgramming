class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        
        tiles.sort()

        def search(index, p):
            l, r = 0, index - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if tiles[mid][1] < p:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        sum_v = [0] * len(tiles)
        res = 0
        for idx, tile in enumerate(tiles):
            sum_v[idx] = sum_v[idx - 1] + tile[1] - tile[0] + 1 if idx > 0 else tile[1] - tile[0] + 1
            p = tile[1] - carpetLen + 1
            index = search(idx, p)
            
            cp = sum_v[idx] - sum_v[index] if index >=0 else sum_v[idx]
            if p - tiles[index + 1][0] >= 0:
                cp -= (p - tiles[index + 1][0])
            res = max(res, cp)
        return res
