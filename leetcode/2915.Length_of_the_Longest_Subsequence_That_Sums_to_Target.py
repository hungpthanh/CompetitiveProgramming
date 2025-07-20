class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * (target + 1)
        dp[0] = 0
        for i in range(n):
            tmp = [-1] * (target + 1)
            for j in range(target + 1):
                if (j >= nums[i]) and (dp[j - nums[i]] != -1):
                    tmp[j] = dp[j - nums[i]] + 1
            for j in range(target + 1):
                dp[j] = max(dp[j], tmp[j])
        
        return dp[target]
