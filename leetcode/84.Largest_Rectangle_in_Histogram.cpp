class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        heights.insert(heights.begin(), 0);
        int L[n + 5], R[n + 5];
        for (int i = 0; i < n + 5; ++i) {
            L[i] = 0;
            R[i] = 0;
        }
        heights.push_back(0);
        stack<int> S; S.push(0);
        for (int i = 1; i <= n + 1; ++i) {
            while ((heights[i] < heights[S.top()])) {
                R[S.top()] = i;
                S.pop();
            }
            if (heights[i] == heights[S.top()]) L[i] = L[S.top()]; else L[i] = S.top();
            S.push(i);
        }
        int ans = 0;
        for (int i = 1; i <= n; ++i) {
            ans = max(ans, heights[i] * (R[i] - L[i] - 1));
        }
        return ans;
    }
};
