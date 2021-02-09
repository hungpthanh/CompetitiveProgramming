class Solution {
public:
    class Fenwick {
        int arr[20005];
        public:
            void init() {
                for (int i = 0; i < 20005; ++i) arr[i] = 0;
            }

            void add(int p, int v) {
                for (int i = p; i < 20005; i += i & (-i)) arr[i] += v;
            }

            int sum(int p) {
                int ans = 0;
                for(int i = p; i; i -= i & -i) ans += arr[i];
                return ans;
            }
    };
    
    static bool cmp(pair<int, int> a, pair<int, int> b) {
        return (a.second < b.second);
    }
    
    vector<int> countSmaller(vector<int>& nums) {
        Fenwick fw = Fenwick();
        fw.init();
        
        vector<pair<int, int> > arr;
        for (int i = 0; i < nums.size(); ++i) {
            arr.push_back(make_pair(nums[i], i));
        }
        sort(arr.begin(), arr.end());
        int v = 1;
        int n = arr.size();
        arr.push_back(make_pair(10005, n + 1));
        for (int i = 0; i < n; ++i) {
            if (arr[i].first != arr[i + 1].first) arr[i].first = v++;
            else arr[i].first = v;
        }
        vector<int> results;
        sort(arr.begin(), arr.end(), cmp);
        for (int i = n - 1; i >= 0; --i) {
            results.push_back(fw.sum(arr[i].first - 1));
            fw.add(arr[i].first, 1);
        }
        reverse(results.begin(), results.end());
        return results;
    }
};
