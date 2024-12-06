class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        n = len(intervals)
        dp = [0] * (n + 1)
        best = [5 * 1e4 + 5] * (n + 1)
        dp[1] = 1
        best[1] = intervals[0][1]
        max_length = 1
        for i in range(2, n + 1):
            dp[i] = 1
            index = bisect.bisect_right(best[1: max_length + 1], intervals[i - 1][0])
            if index >= 1 and best[index] <= intervals[i - 1][0]:
                dp[i] = index + 1
            best[dp[i]] = min(best[dp[i]], intervals[i - 1][1])
            max_length = max(max_length, dp[i])
        return n - max(dp[1:])
