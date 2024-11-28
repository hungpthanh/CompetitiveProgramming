class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        s = "." + s
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range (1, i + 1):
                if s[j: i + 1] in wordDict and dp[j - 1]:
                    dp[i] = True
        return dp[n]
