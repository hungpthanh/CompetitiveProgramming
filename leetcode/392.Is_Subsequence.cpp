class Solution {
public:
    bool isSubsequence(string s, string t) {
        int st_s = 0;
        int st_t = 0;
        for (int i = 0; i < t.size(); ++i) {
            if (t[i] == s[st_s]) ++st_s;
        }
        return (st_s >= s.size());
    }
};
