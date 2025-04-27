class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heights = [heights[i + 1] - heights[i] if heights[i + 1] > heights[i] else 0 for i in range(len(heights) - 1)]
        n = len(heights)
        heap = []
        sum_ladders = 0
        sum_all = 0
        for i in range(n):
            sum_ladders += heights[i]
            sum_all += heights[i]
            if i < ladders:
                heapq.heappush(heap, heights[i])
            else:
                k = heapq.heappushpop(heap, heights[i])
                sum_ladders -= k
            if sum_all - sum_ladders > bricks:
                return i
        return n
