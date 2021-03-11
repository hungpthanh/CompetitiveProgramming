class Solution {
public:
    struct hash_pair { 
    template <class T1, class T2> 
    size_t operator()(const pair<T1, T2>& p) const
    { 
        auto hash1 = hash<T1>{}(p.first); 
        auto hash2 = hash<T2>{}(p.second); 
        return hash1 ^ hash2; 
    } 
}; 
    
    int minAreaRect(vector<vector<int>>& points) {
        unordered_map<pair<int, int>, bool, hash_pair> u_map;
        
        for (int i = 0; i < points.size(); ++i) {
            u_map[make_pair(points[i][0], points[i][1])] = true;
        }
        int res = 1700000000;
        for (int i = 0; i < points.size() - 2; ++i)
            for (int j = i + 1; j < points.size() - 1; ++j)
                if ((points[i][0] != points[j][0]) && (points[i][1] != points[j][1])) {
                    if ((u_map.find(make_pair(points[i][0], points[j][1])) != u_map.end()) && (u_map.find(make_pair(points[j][0], points[i][1])) != u_map.end())) {
                        res = min(res, abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1]));
                    }
                }
        
        if (res == 1700000000) return 0;
        return res;
    }
};
