/*
 * This implementation based on sample 48 ms submission
 */
#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int> &nums, int k) {
        vector<double> results;
        Tracker tracker;
        for (int i = 0; i < nums.size(); ++i) {
            tracker.insert(nums[i]);
            if (i >= k - 1) {
                results.push_back(tracker.get());
                tracker.remove(nums[i - k + 1]);
            }
        }
        return results;
    }

private:
    class Tracker {
    public:
        void insert(int v) {
            q_max.emplace(v);
            q_min.insert(*q_max.begin());
            q_max.erase(q_max.begin());
            if (q_max.size() < q_min.size()) {
                q_max.emplace(*q_min.begin());
                q_min.erase(q_min.begin());
            }
        }

        void remove(int v) {
            if (v <= *q_max.begin()) {
                auto it = q_max.find(v);
                q_max.erase(it);
            } else {
                auto it = q_min.find(v);
                q_min.erase(it);
            }
            if (q_max.size() < q_min.size()) {
                q_max.emplace(*q_min.begin());
                q_min.erase(q_min.begin());
            }
        }

        double get() {
            if (q_min.size() == q_max.size()) return 0.5 * ((double) (*q_min.begin()) + (double) (*q_max.begin()));
            return *q_max.begin();
        }

    private:
        multiset<int> q_min;
        multiset<int, greater<> > q_max;
    };
};

int main() {
    Solution sol;
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<double> results = sol.medianSlidingWindow(nums, k);
    for (auto v: results) cout << v << endl;
}
