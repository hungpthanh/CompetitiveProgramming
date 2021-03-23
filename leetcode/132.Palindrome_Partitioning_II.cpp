class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        s = '0' + s;
        bool isPalindrome[n + 5][n + 5];
        for (int i = 1; i <= n; ++i) isPalindrome[i][i] = true;
        for (int len  = 2; len <= n; ++len) {
            for (int i = 1; i <= n - len + 1; ++i) {
                bool mid_palindrome;
                if (i + 1 > i + len - 2) mid_palindrome = true;
                else mid_palindrome = isPalindrome[i + 1][i + len - 2];
                isPalindrome[i][i + len - 1] = ((mid_palindrome && (s[i] == s[i + len - 1]))? true: false);
            }
        }
        int dp[n + 5];
        dp[1] = 0;
        for (int i = 2; i <= n; ++i) {
            if (isPalindrome[1][i]) dp[i] = 0;
            else dp[i] = n + 5;
            for (int j = 2; j <= i; ++j) 
                if (isPalindrome[j][i]) dp[i] = min(dp[i], dp[j - 1] + 1);
        }
        return dp[n];
    }
};
