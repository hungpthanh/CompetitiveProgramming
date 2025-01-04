class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [-1] * n
        right = [-1] * n
        left[0], right[n - 1] = height[0],  height[n - 1]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
            right[-i - 1] = max(right[-i], height[-i - 1])
        res = 0
        for i in range(1, n - 1):
            bar = min(left[i - 1], right[i + 1])
            if bar > height[i]:
                res += bar - height[i]
        return res
