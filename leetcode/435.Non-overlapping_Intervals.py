class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = 1
            for j in range(i, 0, -1):
                if intervals[j - 1][1] <= intervals[i - 1][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break
        return n - max(dp[1:])
