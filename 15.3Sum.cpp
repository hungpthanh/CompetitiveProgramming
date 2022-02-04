class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        int cons = int(1e5);

        int dd[2 * cons + 5];
        for (int i = 0; i < 2 * cons + 5; ++i) dd[i] = -1;
        sort(nums.begin(), nums.end());
        
        unordered_set<long long> s;
            
        for (int i = 0; i < n; ++i) dd[nums[i] + cons] = i;
        vector<vector<int> > results;

        for (int i = 0; i < n - 2; ++i)
            for (int j = i + 1; j < n - 1; ++j) {
                int remain_v = 0 - nums[i] - nums[j];
                if ((remain_v < -cons) || (remain_v > cons)) continue;
                if ((dd[remain_v + cons] == -1) || ((dd[remain_v + cons] != -1) && (dd[remain_v + cons] <= j))) continue;
                
                if ((s.find( (long long) (nums[i]) * cons * 10 + nums[j])) != s.end()) continue;
                
                s.insert((long long)(nums[i]) * cons * 10 + nums[j]);
                vector<int> tmp = {nums[i], nums[j], remain_v};
                results.push_back(tmp);
            }
        
        return results;
    
    }
};
