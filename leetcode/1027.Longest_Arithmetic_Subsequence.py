class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        maxn = 500
        n = len(nums)
        dp = [[0] * (2 * maxn + 1) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j] + maxn
                dp[i][diff] = dp[j][diff] + 1 if dp[j][diff] > 0 else 2
        return max(max(item) for item in dp)
