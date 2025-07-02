# TLE, sol: binary search results, i.e., the value of k-th
# Using BS to counting number of element 
# The current sol got TLE
class Data:
    def __init__(self, value, i, j):
        self.value = value
        self.i = i
        self.j = j

    def __lt__(self, other):
        """
        Defines the less-than comparison for MyObject instances.
        This determines the order in the heap.
        """
        return self.value < other.value

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        MAX_INT = int(1e10 + 5)
        BASE = int(5 * 1e4) + 5
        def gen(a, b):
            if len(a) > 0 and len(b) > 0:
                added = set()
                heap = [Data(a[0] * b[0], 0, 0)]
                heapq.heapify(heap)
                n, m = len(a), len(b)
                added.add(0)
                while len(heap) > 0:
                    top = heappop(heap)
                    yield top.value
                    i, j = top.i, top.j
                    if i + 1 < n and ((i + 1) * BASE + j) not in added:
                        added.add(((i + 1) * BASE + j))
                        heappush(heap, Data(a[i + 1] * b[j], i + 1, j))
                    if j + 1 < m and (i * BASE + (j + 1)) not in added:
                        added.add((i * BASE + (j + 1)))
                        heappush(heap, Data(a[i] * b[j + 1], i, j + 1))
        num1_pos = [item for item in nums1 if item >= 0]
        num1_neg = [item for item in nums1 if item < 0]
        num2_pos = [item for item in nums2 if item >= 0]
        num2_neg = [item for item in nums2 if item < 0]

        update = [0, 1, 2, 3]
        
        g0 = gen(num1_pos, num2_pos)  # >0, >0
        g1 = gen(num1_neg[::-1], num2_neg[::-1])  # <0, <0
        g2 = gen(num1_pos[::-1], num2_neg)  # >0, <0
        g3 = gen(num1_neg, num2_pos[::-1])  # <0, >0
        g = [g0, g1, g2, g3]
        v = [MAX_INT, MAX_INT, MAX_INT, MAX_INT]

        while k:
            
            for index in update:
                v[index] = next(g[index], MAX_INT)

            if k == 1:
                return min(v)
            
            for index in range(4):
                if min(v) == v[index]:
                    update = [index]
                    break
            k -= 1

