class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        st = 0
        res = 0
        cnt = 0
        last = defaultdict(lambda: -1)
        for i in range(n):
            if last[nums[i]] >= 0:
                res = max(res, cnt)
                current_last = last[nums[i]]
                for j in range(st, last[nums[i]] + 1):
                    last[nums[j]] = -1
                    cnt -= nums[j]
                st = current_last + 1        
            last[nums[i]] = i
            cnt += nums[i]

        res = max(res, cnt)
        return res
