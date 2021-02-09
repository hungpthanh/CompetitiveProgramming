class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> results;
        deque<pair<int, int> > Q;
        for (int i = 0; i < nums.size(); ++i) {
            while ((Q.size() > 0) && (Q.front().second <= i - k) && (i > k - 1)) Q.pop_front();
            while ((Q.size() > 0) && (nums[i] > Q.back().first)) Q.pop_back();
            Q.push_back(make_pair(nums[i], i));
            if (i >= k - 1) results.push_back(Q.front().first);
        }
        return results;
    }
};
