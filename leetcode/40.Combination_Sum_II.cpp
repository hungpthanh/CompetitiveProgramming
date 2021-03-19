class Solution {
public:
    vector<vector<int> > results;
    vector<int> tmp;
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        int ss = 0;
        for (auto c: candidates) ss += c;
        if (ss < target) return results;
        tmp.clear();
        backtrack(0, 0, target, candidates);
        return results;
    }
    
    void backtrack(int i, int sum, int target, vector<int> &candidates) {
        if (sum > target) return;
        if (sum == target) {
            for (auto c: results) {
                if (equal(c.begin(), c.end(), tmp.begin())) return;
            } 
            results.push_back(tmp);
            return;
        }
        if (i >= candidates.size()) return;
        for (int j = 0; j <= 1; ++j) {
            if (j == 1) tmp.push_back(candidates[i]);
            backtrack(i + 1, sum + j * candidates[i], target, candidates);
            if (j == 1) tmp.pop_back();
        }
    }
};
