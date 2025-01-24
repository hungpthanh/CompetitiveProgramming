class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diffs = []
        for i in range(len(nums) - 1):
            diffs.append(nums[i + 1] - nums[i])
        n = len(diffs)
        res = 0
        cnt = 1
        diffs.append(3000)
        for i in range(n):
            if diffs[i] == diffs[i + 1]:
                cnt += 1
            else:
                if cnt >= 2:
                    res += (cnt - 1) * cnt // 2
                cnt = 1
        return res
