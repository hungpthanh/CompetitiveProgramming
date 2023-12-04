class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        int dp[n + 5];
        int res = 0;
        memset(dp, 0, sizeof(dp));
        dp[0] = nums[0];
        res = dp[0];
        for (int i = 1; i < n - 1; ++i) {
            dp[i] = nums[i];
            for (int j = 0; j < i - 1; ++j) dp[i] = max(dp[i], dp[j] + nums[i]);
            res = max(res, dp[i]);
        }
        memset(dp, 0, sizeof(dp));
        dp[1] = nums[1];
        res = max(res, dp[1]);
        for (int i = 2; i < n; ++i) {
            dp[i] = nums[i];
            for (int j = 1; j < i - 1; ++j) dp[i] = max(dp[i], dp[j] + nums[i]);
            res = max(res, dp[i]);
        }
        return res;
    }
};
