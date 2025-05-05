class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = 1
        dp[1][1] = 1
        dp[2][0] = 1
        dp[2][1] = 2
        MOD = int(1e9 + 7)
        for i in range(3, n + 1):
            dp[i][0] = ((dp[i - 2][0] + dp[i - 2][1]) % MOD + (dp[i - 3][1] if i >= 3 else 0) % MOD) % MOD
            dp[i][1] = (dp[i - 1][1] + (2 * dp[i - 1][0]) % MOD + dp[i - 2][1]) % MOD
        # print(dp)
        return dp[n][1]
