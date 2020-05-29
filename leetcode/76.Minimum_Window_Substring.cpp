class Solution {
public:
    string minWindow(string s, string t) {
        int n = t.size();
        int m = s.size();
        t = '0' + t;
        s = '0' + s;
        int max_char = 60;
        int cnt_tr[max_char];
        int cnt_sr[max_char];
        for (int i = 0; i < max_char; ++i) {
                cnt_sr[i] = 0;
                cnt_tr[i] = 0;
        }
        for (int i = 1; i <= n; ++i) {
                cnt_tr[t[i] - 'A'] += 1;
        }
        int satis = 0;
        for (int i = 0; i < max_char; ++i) if (cnt_tr[i] == 0) satis += 1;
        int st = 1;
        int saveL = m + 1, savest = -1, saveen = -1;
        for (int i = 1; i <= m; ++ i) {
            cnt_sr[s[i] - 'A'] += 1;
            if (cnt_sr[s[i] - 'A'] == cnt_tr[s[i] - 'A']) satis += 1;
            while ((satis == max_char) and (st <= i)) {
                if (saveL > i - st + 1) {
                    saveL = i - st + 1;
                    savest = st;
                    saveen = i;
                }
                --cnt_sr[s[st] - 'A'];
                if (cnt_sr[s[st] - 'A'] < cnt_tr[s[st] - 'A']) satis -= 1;
                st += 1;
            }
        }
        if (saveL == m + 1) return "";
        else {
            string ans = "";
            for (int i = savest; i <= saveen; ++i) ans += s[i];
            return ans;
        }
    }
};
