class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        inf = n + 5
        dp = [[0] * 4 for _ in range(n + 1)]
        dp[0][2] = 0
        dp[0][1] = 1 if obstacles[0] != 1 else inf
        dp[0][3] = 1 if obstacles[0] != 3 else inf
        for i in range(1, n + 1):
            for j in range(1, 4):
                if j == obstacles[i]:
                    dp[i][j] = inf
                else:
                    dp[i][j] = dp[i - 1][j]
                    if obstacles[i] != 1:
                        dp[i][j] = min(dp[i][j], dp[i - 1][1] + 1)
                    if obstacles[i] != 2:
                        dp[i][j] = min(dp[i][j], dp[i - 1][2] + 1)
                    if obstacles[i] != 3:
                        dp[i][j] = min(dp[i][j], dp[i - 1][3] + 1)
        return min(dp[n][1:])
