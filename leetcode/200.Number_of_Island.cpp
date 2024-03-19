const vector<int> cx{-1, 1, 0, 0};
const vector<int> cy{0, 0, -1, 1};
bool visited[300 + 5][300 + 5];

class Solution {
public:
    

    void dfs(int i, int j, vector<vector<char>>& grid, int const &m, int const &n) {
        visited[i][j] = true;
        for (int k = 0; k < 4; ++k) {
            int nx = i + cx[k];
            int ny = j + cy[k];
            if (!((0 <= nx) && (nx < m) && (0 <= ny) && (ny < n))) continue;
            if ((!visited[nx][ny]) && (grid[nx][ny] == '1')) dfs(nx, ny, grid, m, n);
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        memset(visited, false, sizeof(visited));
        int ans = 0;
        for (int i = 0; i < m; ++i)  
            for (int j = 0; j < n; ++j)
                if ((!visited[i][j]) && (grid[i][j] == '1')) {
                    ++ans;
                    dfs(i, j, grid, m, n);
                }
        return ans;
    }
};
