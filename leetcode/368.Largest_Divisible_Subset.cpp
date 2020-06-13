class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        if (nums.size() == 0) return nums;
        int res = 0, saveId;
        int dp[nums.size() + 5], track[nums.size() + 5];
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); ++i) {
            dp[i] = 1;
            track[i] = -1;
            for (int j = 0; j < i; ++j) if (nums[i] % nums[j] == 0) {
                if (dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    track[i] = j;
                }
            }
            if (dp[i] > res) {
                res = dp[i];
                saveId = i;
            }
            
        }
        // cout << "res = " << res << endl;
        // cout << "saveId = " << saveId << endl;
        vector<int> result;
        while (saveId != -1) {
            result.push_back(nums[saveId]);
            saveId = track[saveId];
        }
        // for (int i = 0; i < result.size(); ++i) cout << result[i] << " "; cout << endl;
        reverse(result.begin(), result.end());
        return result;
    }
};
