class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        s = '.' + s
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = True
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                if i + k > n:
                    continue
                dp[i][i + k] = (s[i] == s[i + k])
                if (i + k - 1 >= i + 1):
                    dp[i][i + k] &= dp[i + 1][i + k - 1]
        for k in range(n, -1, -1):
            for i in range(1, n + 1):
                if (i + k <= n) and dp[i][i + k]:
                    return s[i: i + k + 1]
        return ""
