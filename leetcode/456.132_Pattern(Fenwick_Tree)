// time: 76 ms
// Mem: 18.3 mb
class Solution {
public:
    int fen[20005];
    int min_v[20005];

    void update(int p, int val){
        for(int i = p; i <= 20000; i += i & -i) fen[i] += val;
    }
    int sum(int p) {
        int ans = 0;
        for(int i = p; i; i -= i & -i)
            ans += fen[i];
        return ans;
    }
    static bool cmp(pair<int, int> pa, pair<int, int> pb) {
        return (pa.second < pb.second);
    }
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        if (n < 3) return false;
        pair<int, int> arr[n + 1];
        for (int i = 0; i < n; ++i) arr[i] = make_pair(nums[i], i);
        sort(arr, arr + n);
        for (int i = 0; i < n; ++i) cout << arr[i].first << " "; cout << endl;
        int last_v = arr[0].first;
        arr[0].first = 1;
        int v = 1;

        for (int i = 1; i < n; ++i) {
            if (arr[i].first != last_v) {
                ++v;
                last_v = arr[i].first;
                arr[i].first = v;
            }
            else arr[i].first = arr[i - 1].first;
        }
        for (int i = 0; i < n; ++i) cout << arr[i].first << " "; cout << endl;
        sort(arr, arr + n, cmp);
        for (int i = 0; i < n; ++i) cout << arr[i].first << " "; cout << endl;
        min_v[0] = arr[0].first;
        for (int i = 1; i < n; ++i) min_v[i] = min(min_v[i - 1], arr[i].first);
        update(arr[n - 1].first, 1);
        for (int i = n - 2; i >= 1; --i) {
            int a_i = min_v[i - 1];
            int nb = sum(arr[i].first - 1) - sum(a_i);
            if (nb > 0) return true;
        }
        return false;
    }
};
