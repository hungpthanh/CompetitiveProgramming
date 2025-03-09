class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, max(time) * totalTrips + 5
        def check(ti):
            trip = 0
            for t in time:
                trip += ti // t
            return trip
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if check(mid) >= totalTrips:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
