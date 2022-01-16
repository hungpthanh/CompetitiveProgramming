class Solution {
public:
    int uniqueLetterString(string s) {
        int last_prefix[30], last_suffix[30];
        int n = s.size();
        int prefix[n + 5], suffix[n + 5];
        
        s = '#' + s;
        for (char i = 'A'; i <= 'Z'; ++i) {
            last_prefix[i - 'A'] = 0;
            last_suffix[i - 'A'] = n + 1;
        }
        
        for (int i = 1; i <= n; ++i) {    
            prefix[i] = last_prefix[s[i] - 'A'];
            last_prefix[s[i] - 'A'] = i;
        }
        for (int i = n; i >= 1; --i) {    
            suffix[i] = last_suffix[s[i] - 'A'];
            last_suffix[s[i] - 'A'] = i;
        }
        long long res = 0;
        for (int i = 1; i <= n; ++i) {
            res += 1LL * (i - prefix[i]) * (suffix[i] - i);
        }
        return res;
    }
};
