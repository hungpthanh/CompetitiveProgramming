class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n - 1
        while (left < right):
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            if ((nums[mid] > nums[n - 1]) and ((target > nums[mid]) or (target < nums[0]))) or ((nums[mid] < nums[n - 1]) and (nums[mid] < target <= nums[n - 1])):
                left = mid + 1
            else:
                right = mid - 1
        if nums[left] == target:
            return left
        return -1
