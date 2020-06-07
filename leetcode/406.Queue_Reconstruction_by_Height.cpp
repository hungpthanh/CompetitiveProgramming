class Solution {
public:
    
    static bool cmp(pair<int, int> a, pair<int, int> b) {
        if (a.second < b.second) return true;
        if (a.second == b.second) return (a.first < b.first);
        return false;
    }
    
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        vector<pair<int, int> > data, result;
        for (int i = 0; i < people.size(); ++i) data.push_back(make_pair(people[i][0], people[i][1]));
        sort(data.begin(), data.end(), cmp);
        for (int i = 0; i < data.size(); ++i) {
            int nb = 0;
            bool ok = false;
            for (auto it = result.begin(); it != result.end(); ++it) {
                if ((*it).first >= data[i].first) ++nb;
                if (nb > data[i].second) {
                    result.insert(it, data[i]);
                    ok = true;
                    break;
                }
            }
            if (!ok) result.insert(result.end(), data[i]);
        }
        
        vector<vector<int> > final_result;
        vector<int> tmp;
        for (int i = 0; i < result.size(); ++i) {
            tmp.clear();
            tmp.push_back(result[i].first);
            tmp.push_back(result[i].second);
            final_result.push_back(tmp);
        }
        return final_result;
    }
};
