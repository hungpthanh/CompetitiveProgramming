class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> results;
        multiset<int> q_min;
        multiset<int> :: iterator it_min;
        multiset<int, greater<int> > q_max;
        multiset<int, greater<int> > :: iterator it_max;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if ((q_min.size() > 0) && (*q_min.begin() <= nums[i])) q_min.insert(nums[i]);
            else q_max.insert(nums[i]);
            
            if (i >= k) {
                int del_v = nums[i - k];
                if (q_max.size() > q_min.size()) {
                    it_max = q_max.find(del_v);
                    if (it_max != q_max.end()) {
                        q_max.erase(it_max);
                    }
                    else {
                        it_min = q_min.find(del_v);
                        q_min.erase(it_min);
                    }
                }
                else {
                    it_min = q_min.find(del_v);
                    if (it_min != q_min.end()) {
                        q_min.erase(it_min);
                    }
                    else {
                        it_max = q_max.find(del_v);
                        q_max.erase(it_max);
                    }
                }
            }
            if (((q_max.size() - q_min.size()) > 1) || ((q_max.size() - q_min.size()) < -1)) {
                if (q_max.size() > q_min.size()) while (q_max.size() > q_min.size()) {
                    q_min.insert(*q_max.begin());
                    q_max.erase(q_max.begin());
                }
                else {
                    while (q_max.size() < q_min.size()) {
                        q_max.insert(*q_min.begin());
                        q_min.erase(q_min.begin());
                    }
                }
            }
            if (i >= k - 1) {
                if (q_max.size() == q_min.size()) {
                    double tmp = *q_max.begin() * 1.0 + *q_min.begin() * 1.0;
                    tmp /= 2;
                    results.push_back(tmp);
                }
                else {
                    if (q_max.size() > q_min.size()) results.push_back(*q_max.begin());
                    else results.push_back(*q_min.begin());
                }
            }
        }
        return results;
    }
};
