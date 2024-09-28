class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        res = min(height[n - 1], height[0]) * (n - 1)
        while (left < right):
            run = 1
            if height[left] <= height[right]:
                while (left + run < n - 1) and (height[left + run] < height[left]): 
                    run += 1
                left += run
            else:
                while (right - run > 0) and (height[right - run] < height[right]): run += 1
                right -= run
            res = max(res, (right - left) * min(height[left], height[right]))
        return res
