class Solution {
public:
    int uniqueLetterString(string s) {
        int n = s.size();
        s = '#' + s;
        pair<int, int> last_position[35];
        for (int i = 1; i <= 30; ++i) last_position[i] = make_pair(0, 0);
        long long sum_at_i = 0;
        long long res = 0;
        for (int i = 1; i <= n; ++i) {
            int first = last_position[s[i] - 'A'].first;
            int second = last_position[s[i] - 'A'].second;
            sum_at_i += (i - first) - (first - second);
            last_position[s[i] - 'A'] = make_pair(i, first);
            res += sum_at_i;
        }
        return res;
    }
};
