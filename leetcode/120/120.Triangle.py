class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                neghbour1 = dp[i - 1][j - 1] if j - 1 >= 0 else int(1e8)
                neghbour2 = dp[i - 1][j] if j <= i - 1 else int(1e8)
                dp[i][j] = min(neghbour1, neghbour2) + triangle[i][j]
        return min(dp[n - 1])