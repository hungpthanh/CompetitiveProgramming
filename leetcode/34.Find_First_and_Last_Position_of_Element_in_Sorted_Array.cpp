class Solution {
public:

    vector<int> searchRange(vector<int>& nums, int target) {
        auto low = lower_bound (nums.begin(), nums.end(), target);
        auto up = upper_bound (nums.begin(), nums.end(), target);
        if (low == nums.end()) return vector<int> {-1, -1};
        if (*low != target) return vector<int> {-1, -1};
        --up;
        int low_pos = int(low - nums.begin());
        int up_pos = int(up - nums.begin());
        return vector<int> {low_pos, up_pos};
    }
};
