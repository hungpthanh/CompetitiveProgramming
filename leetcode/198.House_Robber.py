class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        max_prev = 0
        for i in range(2, n + 1):
            dp[i] = max_prev + nums[i - 1]
            max_prev = max(max_prev, dp[i - 1])
        return max(dp)
