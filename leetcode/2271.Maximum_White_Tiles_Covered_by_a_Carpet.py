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
            
            if p <= tiles[index + 1][0]:
                if index != -1:    
                    res = max(res, sum_v[idx] - sum_v[index])
                else:
                    res = max(res, sum_v[idx])
            else:
                cp = tiles[index + 1][1] - p + 1 + sum_v[idx] - sum_v[index + 2] if index + 2 <= idx else tiles[index + 1][1] - p + 1
                res = max(res, cp)
        return res
