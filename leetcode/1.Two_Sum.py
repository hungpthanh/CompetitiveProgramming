class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        M = {}
        for idx, e in enumerate(nums):
            M[e] = idx
        for idx in range(len(nums)):
            if ((target - nums[idx]) in M) and (M[target - nums[idx]] != idx):
                return [idx, M[target - nums[idx]]]
