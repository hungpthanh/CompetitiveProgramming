class Solution {
public:
    int nb[6] = {0, 0, 1, 8, 6, 9};
    int n;
    string S = "";
    vector<string> results;
    char opposite(char k) {
        if (k == '1') return '1';
        if (k == '6') return '9';
        if (k == '8') return '8';
        if (k == '9') return '6';
        if (k == '0') return '0';
        return '0';
    }
    string build(string S, int isOdd) {
        string ans = S;
        int st;
        st = S.size() - 1;
        if (isOdd) st = S.size() - 2;
        for (int i = st; i >= 0; --i) {
            ans += opposite(S[i]);
        }
        return ans;
    }
    void generate_nb(int i, int n, int isOdd) {
        if (i == n + 1) {
            results.push_back(build(S,isOdd));
            return;
        }
        int st, en;
        st = 1;
        en = 5;
        if (i == 1) st = 2;
        if ((i == n) && (isOdd)) en = 3;
        for (int j = st; j <= en; ++j) {
            S += nb[j] +  '0';
            generate_nb(i + 1, n, isOdd);
            S.pop_back();
        }
    }
    vector<string> findStrobogrammatic(int n) {
        if (n == 1) results = {"0", "1", "8"};
        else {
            int mid = n / 2 + int((n % 2 == 1));
            generate_nb(1, mid, int(n % 2 == 1));
        }
        return results;
    }
};
