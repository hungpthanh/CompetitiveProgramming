class Solution {
    
public:
    const static int maxn = 2e5;
    const static int INF = 1e9;
    int dis[maxn + 5];
    int ret;
    
    int minCostConnectPoints(vector<vector<int>>& points) {
        priority_queue <pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > q;
        
        int n = points.size();
        
        for (int i = 0; i < n; ++i) dis[i] = INF;
        
        dis[0] = 0;
        q.push({0, 0});
        
        while (!q.empty()) {
            pair<int, int> top = q.top(); q.pop();
            int curDis = top.first; int u = top.second;
            
            if (curDis != dis[u]) continue;
            ret += dis[u]; dis[u] = -INF;
            
            for (int v = 0; v < n; ++v) {
                int c = abs(points[v][0] - points[u][0]) + abs(points[v][1] - points[u][1]);
                if (dis[v] > c) {
                    dis[v] = c;
                    q.push({c, v});
                }
            }
        }
        
        return ret;
    }
};
