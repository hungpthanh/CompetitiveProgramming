class Solution {
public:
    int numTrees(int n) {
        int dp[n + 5];
        dp[0] = 1;
        for (int i = 1; i <= n; ++i) {
            dp[i] = 0;
            for (int j = 1; j <= i; ++j) dp[i] += dp[j - 1] * dp[i - j];
        }
        return dp[n];
    }
};
