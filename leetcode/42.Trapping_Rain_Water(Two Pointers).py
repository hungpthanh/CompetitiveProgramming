class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 1, n - 2
        maxLeft, maxRight = height[0], height[n - 1]
        res = 0
        while left <= right:
            if maxLeft < maxRight:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res
