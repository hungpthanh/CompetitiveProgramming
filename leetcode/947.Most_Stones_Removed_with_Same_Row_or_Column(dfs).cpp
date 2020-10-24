class Solution {
public:
    bool dd[1005];
    
    void dfs(int i, const vector<vector<int> > &stones) {
        dd[i] = true;
        int n = stones.size();
        for (int j = 0; j < n; ++j) 
            if ((dd[j] == false) && ((stones[j][0] == stones[i][0]) || (stones[j][1] == stones[i][1]))) dfs(j, stones);
    }
    
    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size();
        for (int i = 0; i < n + 5; ++i) dd[i] = false;
        int cnt = 0;
        for (int i = 0; i < n; ++i) if (dd[i] == false) {
            ++cnt;
            dfs(i, stones);
        }
        return n - cnt;
    }
};
