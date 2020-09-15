class Solution {
public:
    map<string, int> M;
    set<int> dd;
    bool found_t = false;
    double save_v;
    vector<pair<int, double> > adj[200005];
    
    int getID(string s) {
        if (M.find(s) == M.end()) {
            M[s] = M.size() + 1;
        }
        return M[s];
    }
    
    void dfs(int s, int t, double c) {
        if (found_t) return;
        if (s == t) {
            found_t = true;
            save_v = c;
            return ;
        }
        for (int i = 0; i < adj[s].size(); ++i) {
            int u = adj[s][i].first;
            double v = adj[s][i].second;
            if (dd.find(u) != dd.end()) continue;
            dd.insert(u);
            dfs(u, t, c * v);
        }
    }
    
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        int n = equations.size();
        vector<double> ans;
        
        for (int i = 0; i < equations.size(); ++i) {
            int x, y;
            float v;
            x = getID(equations[i][0]);
            y = getID(equations[i][1]);
            v = values[i];
            adj[x].push_back(make_pair(y, v));
            adj[y].push_back(make_pair(x, 1.0 / v));
        }
        
        for (int i = 0; i < queries.size(); ++i) {
            int x, y;
            found_t = false;
            dd.clear();
            if ((M.find(queries[i][0]) == M.end()) || (M.find(queries[i][1]) == M.end())) {
                ans.push_back(-1);
                continue;
            }
            x = getID(queries[i][0]);
            y = getID(queries[i][1]);
            dfs(x, y, 1);
            if (found_t) ans.push_back(save_v);
            else ans.push_back(-1);
        }
        
        return ans;
    }
};
