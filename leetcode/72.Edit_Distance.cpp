class Solution {
public:
    int minDistance(string word1, string word2) {
        word1 = '0' + word1;
        word2 = '0' + word2;
        int n = word1.size();
        int m = word2.size();
        int dp[n + 5][m + 5];
        for (int i = 0; i < n + 5; ++i) for (int j = 0; j < m + 5; ++j) dp[i][j] = 0;
        for (int i = 1; i < n + 5; ++i) dp[i][0] = i;
        for (int i = 1; i < m + 5; ++i) dp[0][i] = i;
        
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <=m; ++j)
                if (word1[i] == word2[j]) dp[i][j] = dp[i - 1][j - 1];
                else {
                    dp[i][j] = min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
                }
        return (dp[n][m]);
    }
};
