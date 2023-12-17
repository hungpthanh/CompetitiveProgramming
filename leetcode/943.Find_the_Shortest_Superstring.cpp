class Solution {
public:
    int getbit(int i, int X) { return (X & (1 << (i - 1))); }
    int onbit(int i, int X) { return (X | (1 << (i - 1))); }
    int offbit(int i, int X) { return ((X | (1 << (i - 1))) - (1 << (i - 1))); }

    int max_substring(const string& s1, const string& s2) {
        int m = s1.size();
        int min_length = min(m, int(s2.size()));
        string suffix_s1, prefix_s2;
        for (int length = min_length; length >= 1; --length) {
            suffix_s1 = s1.substr(m - length, length);
            prefix_s2 = s2.substr(0, length);
            if (suffix_s1 == prefix_s2) return length;
        }
        return 0;
    }
    
    string shortestSuperstring(vector<string>& words) {
        int inf = int(1e8) + 5;
        int n = words.size();
        pair<int, int> trace[(1 << 12) + 5][15];
        int dp[(1 << 12) + 5][15];
        memset(dp, inf, sizeof(dp));

        for (int mask = 1; mask <= (1 << n) - 1; ++mask) 
            for (int i = 1; i <= n; ++i) 
                if (getbit(i, mask) > 0) {
                    dp[mask][i] = inf;
                    int new_mask = offbit(i, mask);
                    if (new_mask == 0) {
                        dp[mask][i] = words[i - 1].size();
                        trace[mask][i] = make_pair(0, words[i - 1].size()); 
                        continue;
                    }
                    for (int j = 1; j <= n; ++j) if (getbit(j, new_mask) > 0) {
                        int max_sub = max_substring(words[j - 1], words[i - 1]);
                        if (dp[mask][i] > dp[new_mask][j] + words[i - 1].size() - max_sub) {
                            dp[mask][i] = dp[new_mask][j] + words[i - 1].size() - max_sub;
                            trace[mask][i] = make_pair(j, words[i - 1].size() - max_sub);
                        }
                    }

                }

        int max_sub, last = 1;
        for (int i = 1; i <= n; ++i) if (dp[(1 << n) - 1][i] < dp[(1 << n) - 1][last]) last = i;

        int mask = (1 << n) - 1;
        string ans = "";
        while (mask > 0) {
            max_sub = trace[mask][last].second;
            ans = words[last - 1].substr(words[last - 1].size() - max_sub, max_sub) + ans;
            mask = offbit(last, mask);
            last = trace[onbit(last, mask)][last].first;
        }
        return ans;
    }
};
