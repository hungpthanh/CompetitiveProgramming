class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heights = [heights[i + 1] - heights[i] if heights[i + 1] > heights[i] else 0 for i in range(len(heights) - 1)]
        n = len(heights)
        ans = 0
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if ladders >= mid + 1:
                ans = mid + 1
                l = mid + 1
            else:
                temp = heights[:mid + 1]
                temp.sort()
                s = sum(temp) if ladders == 0 else sum(temp[:-ladders])
                if s <= bricks:
                    ans = mid + 1
                    l = mid + 1
                else:
                    r = mid - 1
        return ans
