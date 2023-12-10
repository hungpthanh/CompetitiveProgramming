class Solution {
public:
    bool visited[105];

    long long distance(int a, int b, int x, int y) {
        return 1ll * (a - x) * (a - x) + 1ll * (b - y) * (b - y);
    }

    void dfs(int u, vector<vector<int>>& bombs) {
        visited[u] = true;
        int n = bombs.size();
        for (int i = 0; i < n; ++i)
            if (!visited[i]) {
                int a = bombs[u][0];
                int b = bombs[u][1];
                int x = bombs[i][0];
                int y = bombs[i][1];
                long long dis = distance(a, b, x, y);
                if (dis <= 1ll * bombs[u][2] * bombs[u][2]) dfs(i, bombs);
            }
    }

    int maximumDetonation(vector<vector<int>>& bombs) {
        int n = bombs.size();
        int res = 0;
        for (int i = 0; i < n; ++i) {
            memset(visited, false, sizeof(visited));
            dfs(i, bombs);
            int n_bom = 0;
            for (int j = 0; j < n; ++j) if (visited[j]) n_bom += 1;
            res = max(res, n_bom);
        }
        return res;
    }
};
