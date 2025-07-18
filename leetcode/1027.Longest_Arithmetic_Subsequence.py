class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxn = 500
        P = [[0] * (2 * maxn + 1) for _ in range(maxn + 1)]
        P[nums[0]] = [1] * (2 * maxn + 1)
        for i in range(1, n):
            tmp = [1] * (2 * maxn + 1) 
            for k in range(2 * maxn + 1):
                r = nums[i] - k + maxn
                if 0 <= r <= maxn:
                    tmp[k] = P[r][k] + 1
            for k in range(2 * maxn + 1):
                P[nums[i]][k] = max(P[nums[i]][k], tmp[k])
        return max(max(item) for item in P)
                
