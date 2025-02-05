class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        data = []
        for interval in intervals:
            data.append((interval[0], -1, interval[1] - interval[0] + 1))
            data.append((interval[1], 1, interval[1] - interval[0] + 1))
        for idx, query in enumerate(queries):
            data.append((query, 0, idx))
        data.sort(key=lambda x: (x[0], x[1]))

        heap = []
        heapq.heapify(heap)
        count = defaultdict(int)
        ans = [0] * len(queries)
        for item in data:
            point, tp, value = item
            if tp == -1:
                if count[value] == 0:
                    heapq.heappush(heap, value)
                count[value] += 1
            if tp == 1:
                if count[value] > 0:
                    count[value] -= 1
            if tp == 0:
                while heap and count[heap[0]] == 0:
                    heapq.heappop(heap)
                ans[value] = heap[0] if len(heap) > 0 else -1
                
        return ans
