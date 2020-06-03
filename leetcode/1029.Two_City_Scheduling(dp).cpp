class Solution {
public:
    
    
    int twoCitySchedCost(vector<vector<int>>& costs) {
        
        int n = costs.size();
        int dp[n + 5][n + 5];
        dp[0][0] = 0;
        for (int i = 1; i <= n; ++i) dp[0][i] = int(1e9);
        for (int i = 1; i <= n; ++i) {
            dp[i][0] = dp[i - 1][0] + costs[i - 1][1];
            for (int j = 1; j <= i; ++j) dp[i][j] = min(dp[i - 1][j - 1] + costs[i - 1][0], dp[i - 1][j] + costs[i - 1][1]);
            for (int j = i + 1; j <= n; ++j) dp[i][j] = int(1e9);
        }
        return dp[n][int(n / 2)];
    }
};
