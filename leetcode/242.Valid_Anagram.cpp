class Solution {
public:
    bool isAnagram(string s, string t) {
        int cnt[30];
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < s.size(); ++i) ++cnt[s[i] - 'a'];
        for (int i = 0; i < t.size(); ++i) --cnt[t[i] - 'a'];
        for (int i = 0; i < 30; ++i) if (cnt[i] != 0) return false;
        return true;
    }
};
