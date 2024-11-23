class Solution:
    def numDecodings(self, s: str) -> int:
        def is_valid(s):
            if len(s) == 1 and 1 <= int(s[0]) <= 9:
                return True
            if len(s) == 2 and s[0] != '0' and 10 <= int(s) <= 26:
                return True
            return False

        n = len(s)
        s = '.' + s
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if is_valid(s[i]):
                dp[i] += dp[i - 1]
            if (i > 1) and is_valid(s[i - 1: i + 1]):
                dp[i] += dp[i - 2]
        return dp[n]
