class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_s = 0
        res = -int(3e9)
        cur_s = 0
        for num in nums:
            cur_s += num
            res = max(res, cur_s - min_s)
            min_s = min(min_s, cur_s)
        return res
