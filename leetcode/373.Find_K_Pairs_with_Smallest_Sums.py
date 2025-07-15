class Data:
    __slots__ = ['value', 'i', 'j']  # Avoid dynamic __dict__ creation for speed
    def __init__(self, value, i, j):
        self.value = value
        self.i = i
        self.j = j

    def __lt__(self, other):
        return self.value < other.value

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        MAX_INT = 10**10  # much bigger than any product
        def gen(a, b):
            if not a or not b:
                while True:
                    yield MAX_INT
            heap = [Data(a[0] + b[0], 0, 0)]
            heapq.heapify(heap)
            visited = set()
            visited.add((0, 0))
            n, m = len(a), len(b)

            while heap:
                top = heapq.heappop(heap)
                yield [a[top.i], b[top.j]]
                i, j = top.i, top.j
                if i + 1 < n and (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    heapq.heappush(heap, Data(a[i + 1] + b[j], i + 1, j))
                if j + 1 < m and (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    heapq.heappush(heap, Data(a[i] + b[j + 1], i, j + 1))
        
        g = gen(nums1, nums2)
        results = [next(g) for _ in range(k)]
        return results
