class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(n, arr):
            dp = [0] * n
            for i in range(n):
                dp[i] = 1
                for j in range(i):
                    if arr[i] > arr[j]:
                        dp[i] = max(dp[i], dp[j] + 1)    
            return dp
        
        ldp = dp(n, nums)
        rdp = dp(n, nums[::-1])
        res = n
        for i in range(n):
            if ldp[i] >= 2 and rdp[n - 1 - i] >= 2:
                left = max(0, i + 1 - ldp[i])
                right = max(0, n - i - rdp[n - 1 - i])
                res = min(res, left + right)
        return res
