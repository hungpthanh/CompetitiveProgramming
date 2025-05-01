# IDEA: convert one of 1 blocks to 0 / the sum 2 adj 0 block is max -> using RMQ
import math

import math

class RangeMinimumQuery:
    def __init__(self, arr):
        """
        arr: list of size n + 2, but valid range is from index 1 to n
        """
        self.arr = arr
        self.n = len(arr) - 2  # since arr has size n + 2
        self._build_sparse_table()

    def _build_sparse_table(self):
        n = self.n
        k = int(math.log2(n)) + 1
        self.st = [[0] * k for _ in range(n + 1)]

        # Initialize for intervals of length 1
        for i in range(1, n + 1):
            self.st[i][0] = i

        # Build the sparse table
        for j in range(1, k):
            for i in range(1, n - (1 << j) + 2):
                left = self.st[i][j - 1]
                right = self.st[i + (1 << (j - 1))][j - 1]
                self.st[i][j] = left if self.arr[left] <= self.arr[right] else right

    def query(self, l, r):
        """
        Returns the index of the minimum value in arr[l..r], with 1-based indexing
        """
        if l < 1 or r > self.n or l > r:
            raise ValueError("Query range must be within 1 to n and l <= r")
        length = r - l + 1
        j = int(math.log2(length))
        left = self.st[l][j]
        right = self.st[r - (1 << j) + 1][j]
        return left if self.arr[left] <= self.arr[right] else right


class Solution:

    def create_segments(self, n, s):
        segments = [[0, 0]]
        add = True
        for i in range(1, n + 1):
            if s[i] == '0':
                add = True
            else:
                if add:
                    segments.append([i, i])
                    add = False
                else:
                    segments[-1][1] = i
        segments.append([n + 1, n + 1])
        return segments

    def create_active(self, m, segments):
        active = [0] * (m + 2)
        for i in range(1, m + 1):
            active[i] = segments[i + 1][0] - segments[i - 1][1] - 1
        return active

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        s = '1' + s + '1'
        segments = self.create_segments(n, s)
        m = len(segments) - 2  # don't count guardian
        actives = self.create_active(m, segments)  
        rmg = RangeMinimumQuery(actives)
        
        res = []
        return res
