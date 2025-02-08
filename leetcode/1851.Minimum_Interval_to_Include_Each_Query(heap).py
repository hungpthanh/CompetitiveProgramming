class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(q, idx) for idx, q in enumerate(queries)]
        queries.sort()
        intervals.sort(key=lambda x: (x[0], x[1]))
        heap = []
        heapq.heapify(heap)
        index = 0
        ans = [0] * len(queries)
        for query, idx in queries:
            while (index < len(intervals)) and (intervals[index][0] <= query):
                heapq.heappush(heap, (intervals[index][1] - intervals[index][0] + 1, intervals[index][1]))
                index += 1
            while heap and (heap[0][1] < query):
                heapq.heappop(heap)
            
            ans[idx] = heap[0][0] if heap else -1
        return ans
