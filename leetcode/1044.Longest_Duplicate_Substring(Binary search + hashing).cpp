class Solution {
int maxn = 1e5 + 5;
int BASE = 1e7 + 7;
int BASE2 = 1e9 + 9;
int cs1 = 29;
int cs2 = 107;
public:
    string returnDouble(const string &S, int n, int K) {
        pair<long long, long long> h;
        vector<pair<pair<long long, long long>, int> > res;
        long long pw1, pw2;
        pw1 = 1;
        pw2 = 1;
        for (int i = 1; i < K; ++i) {
            pw1 = (pw1 * cs1) % BASE;
            pw2 = (pw2 * cs2) % BASE;
        }
        long long tmpH1 = 0, tmpH2 = 0;
        for (int i = 1; i <= K; ++i) {
            tmpH1 = ((tmpH1 * cs1) % BASE + S[i] - 'a' + 1) % BASE;
            tmpH2 = ((tmpH2 * cs2) % BASE + S[i] - 'a' + 1) % BASE;
        }
        res.push_back(make_pair(make_pair(tmpH1, tmpH2), 1));
        for (int i = 2; i <= n - K + 1; ++i) {
            tmpH1 = (tmpH1 - ((long long)(1) * (S[i - 1] - 'a' + 1) * pw1) % BASE + BASE) % BASE;
            tmpH2 = (tmpH2 - ((long long)(1) * (S[i - 1] - 'a' + 1) * pw2) % BASE + BASE) % BASE;
            tmpH1 = ((tmpH1 * cs1) % BASE + (S[i + K - 1] - 'a' + 1)) % BASE;
            tmpH2 = ((tmpH2 * cs2) % BASE + (S[i + K - 1] - 'a' + 1)) % BASE;
            res.push_back(make_pair(make_pair(tmpH1, tmpH2), i));

        }
        sort(res.begin(), res.end());
        string result = "";
        for (int i = 0; i < res.size() - 1; ++i) if (res[i].first == res[i + 1].first) {
            for (int j = res[i].second; j <= res[i].second + K - 1; ++j) result += S[j];
            return result;
        }
        return result;
    }

    string longestDupSubstring(string S) {
        int n = S.size();
        S = '0' + S;
        int l = 1, r = n, mid;
        string ans = "";
        string check = "";
        while (l <= r) {
            mid = (l + r) >> 1;
            check = returnDouble(S, n, mid);
            if (check != "") {
                ans = check;
                l = mid + 1;
            }
            else r = mid - 1;
        }
        return ans;
    }
};
