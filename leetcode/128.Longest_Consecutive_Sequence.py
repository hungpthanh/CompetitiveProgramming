class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        res = 1
        for item in nums:
            if not (item - 1) in nums:
                current_length = 1
                while (item + current_length) in nums:
                    current_length += 1
                res = max(res, current_length)
        return res

        
