class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * k for _ in range(n)]
        for i in range(n):
            for j in range(i):
                t = (nums[i] % k + nums[j] % k) % k
                dp[i][t] = max(dp[i][t], dp[j][t] + 1)
        return max(max(row) for row in dp) + 1
        
