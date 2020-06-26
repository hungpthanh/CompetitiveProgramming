class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for (int i = 1; i < nums.size(); ++i) {
            for (int j = 0; j < i; ++j) 
                if (nums[i] == nums[j]) return nums[i];
        }
        return nums[0];
    }
};
