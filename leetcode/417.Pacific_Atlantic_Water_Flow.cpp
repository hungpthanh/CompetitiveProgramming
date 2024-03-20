class Solution {
public:
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    bool pa[205][205], ao[205][205];

    void dfs(int i, int j, vector<vector<int>>& heights, int n, int m, bool occean[205][205]) {
        occean[i][j] = true;
        for (int k = 0; k < 4; ++k) {
            int nx = i + dx[k];
            int ny = j + dy[k];
            if ((nx < 0) || (nx >= n) || (ny < 0) || (ny >= m)) continue;
            if ((heights[nx][ny] >= heights[i][j]) && (!occean[nx][ny])) dfs(nx, ny, heights, n, m, occean);
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int n = heights.size();
        int m = heights[0].size();

        memset(pa, false, sizeof(pa));
        memset(ao, false, sizeof(ao));
        // Search for Pacific Ocean
        for (int i = 0; i < n; ++i) if (!pa[i][0]) dfs(i, 0, heights, n, m, pa);
        for (int j = 0; j < m; ++j) if (!pa[0][j]) dfs(0, j, heights, n, m, pa);
        // Search for Atlantic Ocean
        for (int i = 0; i < n; ++i) if (!ao[i][m - 1]) dfs(i, m - 1, heights, n, m, ao);
        for (int j = 0; j < m; ++j) if (!ao[n - 1][j]) dfs(n - 1, j, heights, n, m, ao);
        vector<vector <int> > ans;
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) if (pa[i][j] && ao[i][j]) ans.push_back(vector<int> {i, j});
        return ans;
    }
};
