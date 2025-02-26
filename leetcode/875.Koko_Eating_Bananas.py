class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            t = 0
            for pile in piles:
                t += math.ceil(pile / k)
            return t <= h
        l, r = 1, int(1e9 + 5)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
