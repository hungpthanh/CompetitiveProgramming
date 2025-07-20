class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(2)]
        for i in range(n):
            tmp = [0] * 2
            for k in range(2):
                r = (k - nums[i] % 2 + 2) % 2
                tmp[k] = dp[r][k] + 1
            for k in range(2):
                dp[nums[i] % 2][k] = max(dp[nums[i] % 2][k], tmp[k])
        return max(max(item) for item in dp)
