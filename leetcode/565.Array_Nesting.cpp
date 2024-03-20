vector <int> length;
vector <bool> visited;

class Solution {
public:
    void dfs(int k, const vector<int> & nums) {
        visited[k] = true;
        if (!visited[nums[k]]) {
            dfs(nums[k], nums);
            length[k] = length[nums[k]] + 1;
        }
        else length[k] = 1;
    }

    int arrayNesting(vector<int>& nums) {
        int n = nums.size();
        length.resize(nums.size());
        visited.resize(nums.size());
        for (int i = 0; i < n; ++i) {
            length[i] = 1;
            visited[i] = false;
        }

        for (int i = 0; i < n; ++i) if (!visited[i]) dfs(i, nums);
        int ans = 1;
        for (int i = 0; i < n; ++i) ans = max(ans, length[i]);
        return ans;
    }
};
