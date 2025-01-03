class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        sum_h = [0] * n
        sum_h[0] = height[0]
        for i in range(1, n):
            sum_h[i] = sum_h[i - 1] + height[i]
        l = [-1] * n
        r = [-1] * n
        maxLeft = height[0]
        for i in range(1, n):
            if height[i] < maxLeft:
                l[i] = 1
            else:
                maxLeft = height[i]
        maxRight = height[n - 1]
        for i in range(n - 2, -1, -1):
            if height[i] < maxRight:
                r[i] = 1
            else:
                maxRight = height[i]
        pos = []
        for i in range(n):
            if l[i] == -1 or r[i] == -1:
                pos.append(i)
        m = len(pos)
        res = 0
        for i in range(m - 1):
            res += min(height[pos[i]], height[pos[i + 1]]) * (pos[i + 1] - pos[i] - 1) - sum_h[pos[i + 1] - 1] + sum_h[pos[i]]
        return res
