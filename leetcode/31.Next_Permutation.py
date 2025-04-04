# TODO
# IDEA: The next permution is the smallest number that >= current permution
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
                if nums[i] > nums[st - 1] and nums[i] <= nums[pos]:
                    pos = i
            nums[st - 1], nums[pos] = nums[pos], nums[st - 1]
        en = n - 1
        while st <= en:
            nums[st], nums[en] = nums[en], nums[st]
            st += 1
            en -= 1
        
