class Solution {
public:
    string minWindow(string s, string t) {
        int cnt[60], dd[60];
        deque<int> dq;
        memset(dd, 0, sizeof(dd));
        memset(cnt, 0, sizeof(cnt));
        int save_st = -1;
        int save_en = -1;
        int save_length = (int)(1e5 + 5);
        int current = 0;
        for (int i = 0; i < t.size(); ++i) ++dd[t[i] - 'A'];
        for (int i = 0; i < 60; ++i) if (dd[i] == 0) ++current;
        for (int i = 0; i < s.size(); ++i) {
            ++cnt[s[i] - 'A'];
            dq.push_back(i);
            if (cnt[s[i] - 'A'] == dd[s[i] - 'A']) ++current;
            if (current == 60) {
                while ((current == 60) and !dq.empty()) {
                    if (dq.back() - dq.front() + 1 < save_length) {
                        save_length = dq.back() - dq.front() + 1;
                        save_st = dq.front();
                        save_en = dq.back();
                    }
                    int st = dq.front();
                    --cnt[s[st] - 'A'];
                    if (cnt[s[st] - 'A'] == dd[s[st] - 'A'] - 1) --current;
                    dq.pop_front();
                }
            }
        }
        string result = "";
        if (save_st != -1) result = s.substr(save_st, save_length);
        return result;
    }
};
