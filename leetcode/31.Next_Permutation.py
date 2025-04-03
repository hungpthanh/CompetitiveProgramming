# TODO
# IDEA: The next permution is the smallest number that >= current permution
# Please improve sort part, just reverse
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        st = n - 1
        while (st >= 1) and (nums[st] <= nums[st - 1]):
            st -= 1
        if st != 0:
            pos = st
            for i in range(st, n):
                if nums[i] > nums[st - 1] and nums[i] < nums[pos]:
                    pos = i
            nums[st - 1], nums[pos] = nums[pos], nums[st - 1]
        for i in range(st, n - 1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        
