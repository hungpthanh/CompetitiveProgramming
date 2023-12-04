class Solution {
public:
    vector<vector<pair<int, int> > > adj;
    int d[300];
    bool mark[300];
    const int MAX = int(8 * 1e5) + 5;


    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        adj.resize(n + 1);
        for (auto e: times) adj[e[0]].push_back(make_pair(e[1], e[2]));
        for (int i = 1; i <= n; ++i) d[i] = MAX;
        d[k] = 0;
        for (int i = 1; i <= n; ++i) {
            int d_max = MAX, save_u = -1;
            for (int j = 1; j <= n; ++j) if ((!mark[j]) and (d[j] < d_max)) {
                d_max = d[j];
                save_u = j;
            }
            if (save_u == -1) break;
            mark[save_u] = true;
            for (auto v: adj[save_u]) {
                if (d[v.first] > d[save_u] + v.second) d[v.first] = d[save_u] + v.second;
            }
        }
        int ans = 0;
        for (int i = 1; i <= n; ++i) ans = max(ans, d[i]);   
        if (ans == MAX) ans = -1;
        return ans;
    }   
};
