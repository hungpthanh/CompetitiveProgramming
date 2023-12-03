class Solution {
public:
    int height[int(2 * 10e4 + 1)], prev[int(2 * 10e4 + 1)], save_prev[int(2 * 10e4 + 1)];
    vector<int> adj[int(2 * 10e4 + 1)];
    int visited[int(2 * 10e4 + 1)];

    void dfs(int u, vector<vector<int>>& edges) {
        if (visited[u] == 1) return;
        visited[u] = 1;

        for (auto v: adj[u]) if (visited[v] == 0) {
            prev[v] = u;
            height[v] = height[u] + 1;
            dfs(v, edges);
        }
        
    }
    vector<int> trace_v(int v) {
        vector<int> results;    
        while (prev[v] != -1) {
            results.push_back(v);
            v = prev[v];
        }
        results.push_back(v);
        return results;
    }

    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {

        for (auto edge: edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }        
        vector<int> results;
        results.clear();

        for (int i = 0 ; i < n; ++i) height[i] = 0;
        for (int i = 0 ; i < n; ++i) prev[i] = 0;
        for (int i = 0 ; i < n; ++i) visited[i] = 0;
        int start_u = 0;
        prev[start_u] = -1;
        dfs(start_u, edges);
        
        int save_u = 0, save_h = 0;
        for (int i = 0; i < n; ++i) if (height[i] > save_h) {
            save_h = height[i];
            save_u = i;
        }
        for (int i = 0; i < n; ++i) save_prev[i] = prev[i];
        
        vector<int> trace_v1 = trace_v(save_u);
        // for (auto v: trace_v1) cout << v << " "; cout << endl;
        for (int i = 0 ; i < n; ++i) height[i] = 0;
        for (int i = 0 ; i < n; ++i) prev[i] = 0;
        for (int i = 0 ; i < n; ++i) visited[i] = 0;
        start_u = save_u;
        prev[start_u] = -1;
        dfs(start_u, edges);
        save_u = 0; save_h = 0;
        for (int i = 0; i < n; ++i) if (height[i] > save_h) {
            save_h = height[i];
            save_u = i;
        }

        // for (int i = 0; i < n; ++i) prev[i] = save_prev[i];
        vector<int> trace_final;
        trace_final = trace_v(save_u);
        // if (save_u != 0) trace_final = trace_v(save_u);
        // else trace_final = trace_v(start_u);
        
        int m = trace_final.size();      
        if (m % 2 == 1) results.push_back(trace_final[int(m / 2)]);
        else {
            results.push_back(trace_final[int(m / 2) - 1]);
            results.push_back(trace_final[int(m / 2)]);
        }
        return results;
    }
};
