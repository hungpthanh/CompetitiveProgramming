class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[amount + 5] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            dp[i][0] = 0
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j - coins[i - 1] >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)
        if dp[n][amount] == amount + 5:
            return -1
        return dp[n][amount]
