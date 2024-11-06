class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        d = [0] * len(nums)
        subsets = []
        def select(index):
            if index == len(nums):
                subset = [num for num, mask in zip(nums, d) if mask]
                subsets.append(subset)
                return
            for i in range(2):
                d[index] = i
                select(index + 1)
        select(0)
        return subsets
