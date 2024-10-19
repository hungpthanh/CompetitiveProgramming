class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if mid == 0 or mid == len(nums) - 1:
                return min(nums[left], nums[right])
            if (1 <= mid < len(nums) - 1) and (nums[mid] < nums[mid - 1]) and (nums[mid] < nums[mid + 1]):
                return nums[mid]
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]
            
