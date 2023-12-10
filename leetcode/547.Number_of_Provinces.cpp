class Solution {
public:
    bool visited[305];
    void dfs(int u, vector<vector<int>>& isConnected) {
        visited[u] = true;
        int n = isConnected.size();
        for (int i = 0; i < n; ++i)
            if ((!visited[i]) && (isConnected[u][i])) dfs(i, isConnected);
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size(), ans = 0;
        for (int i = 0; i < n; ++i) visited[i] = false;    
        for (int i = 0; i < n; ++i)
            if (!visited[i]) {
                ans += 1;
                dfs(i, isConnected);
            }
        return ans;
    }
};
