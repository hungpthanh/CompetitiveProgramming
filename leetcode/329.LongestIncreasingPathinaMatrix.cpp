class Solution {
public:
    int csx[4] = {0, 0, -1, 1};
    int csy[4] = {-1, 1, 0 , 0};
    
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        vector<pair<int, pair<int, int> > > Q;
        int n = matrix.size();
        if (n == 0) return 0;
        int m = matrix[0].size();
        int dp[n + 5][m + 5];
        memset(dp, 0, sizeof(dp));
        for (int i = 0; i < n; ++i) 
            for (int j = 0; j < m; ++j) dp[i][j] = 1;
        
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                pair<int, pair<int, int> > v;
                v = make_pair(matrix[i][j], make_pair(i, j));
                Q.push_back(v);
            }
        
        sort(Q.begin(), Q.end());
        
        for (int i = 0; i < Q.size(); ++i) {
            for (int j = 0; j < 4; ++j) {
                int x = Q[i].second.first + csx[j];
                int y = Q[i].second.second + csy[j];
                if ((x < 0) || (x >= n) || (y < 0) || (y >= m)) continue;
                if (Q[i].first <= matrix[x][y]) continue;
                dp[Q[i].second.first][Q[i].second.second] = max(dp[Q[i].second.first][Q[i].second.second], dp[x][y] + 1);
            }    
        }
        int res = 1;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) res = max(res, dp[i][j]);
        return res;
    }
};
