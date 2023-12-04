class Solution {
public:
    const long long c1 = 29;
    const long long MOD = 1000000003;
    long long power1[int(5 * 1e4) + 5], hash1[int(5 * 1e4) + 5], power2[int(5 * 1e4) + 5], hash2[int(5 * 1e4) + 5];

    long long getHash(int i, int j, long long *hash, long long *power) {
        long long x = (hash[j] - hash[i - 1] * power[j - i + 1] + MOD * MOD) % MOD;
        return x;
    }

    string shortestPalindrome(string s) {
        if (s.size() == 1) return s;
        string s1 = s;
        reverse(s1.begin(), s1.end());
        int n = s.size();
        s = "." + s; s1 = "." + s1;
        int m = (int)(n / 2) + (n % 2);

        power1[0] = 1;
        power2[0] = 1;

        for (int i = 1; i <= n; ++i) {            
            power1[i] = (power1[i - 1] * c1) % MOD;
            power2[i] = (power2[i - 1] * c1) % MOD;
        }
        hash1[0] = 0; hash2[0] = 0;
        for (int i = 1; i <= n; ++i) {
            hash1[i] = (hash1[i - 1] * c1 + s[i] - 'a') % MOD;
            hash2[i] = (hash2[i - 1] * c1 + s1[i] - 'a') % MOD;
        }
        for (int i = m; i >= 1; --i) {
            if (((i < m) || (i == m && n % 2 == 0)) && (getHash(i + 1, 2 * i, hash1, power1) == getHash(n + 1 - i, n, hash2, power2))) {
                string se = s.substr(i + 1, n - i);
                reverse(se.begin(), se.end());
                string ans = se + s.substr(i + 1, n - i);
                return ans;
            }

            if ((i > 1) && (getHash(i + 1, 2 * i - 1, hash1, power1) == getHash(n + 1 - (i - 1), n, hash2, power2))) {
                string se = s.substr(i + 1, n - i);
                reverse(se.begin(), se.end());
                string ans = se + s[i] + s.substr(i + 1, n - (i + 1) + 1);
                return ans;
            }
            
        }
        return s1.substr(1, n - 1) + s.substr(1, n);
    }
};
