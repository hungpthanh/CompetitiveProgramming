class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        index = 0
        ans = 0
        while index < len(nums):
            start = index
            ans += 1
            while (start < len(nums)) and (nums[start] <= nums[index] + k):
                start += 1
            index = start
        return ans
