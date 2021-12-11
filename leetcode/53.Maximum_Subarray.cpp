class Solution {
public:
    void divideAndconquer(vector<int>& nums, int l, int r, int &sum, int &prefix, int &suffix, int &max_sum) {
        if (l == r) {
            sum = nums[l];
            prefix = nums[l];
            suffix = nums[l];
            max_sum = nums[l];
            return;
        }
        int mid = (l + r) >> 1;
        int sum_left, sum_right, prefix_left, prefix_right, suffix_left, suffix_right, max_sum_left, max_sum_right;
        divideAndconquer(nums, l, mid, sum_left, prefix_left, suffix_left, max_sum_left);
        divideAndconquer(nums, mid + 1, r, sum_right, prefix_right, suffix_right, max_sum_right);
        sum = sum_left + sum_right;
        prefix = max(prefix_left, sum_left + prefix_right);
        suffix = max(suffix_right, sum_right + suffix_left);
        max_sum = max(max(max_sum_left, max_sum_right), suffix_left + prefix_right);
    }
    
    int maxSubArray(vector<int>& nums) {
        int sum, prefix, suffix, max_sum;
        int sz = nums.size();
        divideAndconquer(nums, 0, sz - 1, sum, prefix, suffix, max_sum);
        return max_sum;
    }
};
