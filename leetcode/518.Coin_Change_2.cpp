
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        if (coins.size() == 0) {
            if (amount == 0) return 1;
            return 0;
        }
        int dp[amount + 5][coins.size() + 5];
        int sum[amount + 5][coins.size() + 5];
        
        memset(dp, 0, sizeof(dp));
        memset(sum, 0, sizeof(sum));
        for (int i = 0; i < coins.size(); ++i) {
            dp[0][i] = 1;
            sum[0][i] += 1;
        }
        for (int i = 1; i <= amount; ++i) {
            for (int j = 0; j < coins.size(); ++j) if (i >= coins[j]) dp[i][j] += sum[i - coins[j]][j];
            for (int j = 0; j < coins.size(); ++j) {
                if (j > 0) sum[i][j] = sum[i][j - 1] + dp[i][j];
                else sum[i][j] = dp[i][j];
            }
        }
        
        return sum[amount][coins.size() - 1];
    }
};
