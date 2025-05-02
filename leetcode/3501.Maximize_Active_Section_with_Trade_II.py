# IDEA: convert one of 1 blocks to 0 / the sum 2 adj 0 block is max -> using RMQ
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
                self.st[i][j] = left if self.arr[left] >= self.arr[right] else right

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
        return left if self.arr[left] >= self.arr[right] else right


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
        left = [item[0] for item in segments]
        right = [item[1] for item in segments]
        return segments, left, right

    def create_active(self, m, segments):
        active = [0] * (m + 2)
        for i in range(1, m + 1):
            if segments[i + 1][0] - segments[i][1] >= 2 and segments[i][0] - segments[i - 1][1] >= 2:
                active[i] = segments[i + 1][0] - segments[i - 1][1] - 1 - (segments[i][1] - segments[i][0] + 1)
        return active

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        # maybe better don't keep segment of pair, just 2 list of st and en because search on left and right 
        # based on st and en respectively // no use key function -> Done
        n = len(s)
        s = '1' + s + '1'

        su = [0] * (n + 2)
        for i in range(1, n + 1):
            # print(s[i])
            su[i] = su[i - 1] + (1 if s[i] == '1' else 0)
        # print(f"su: {su}")
        segments, left, right = self.create_segments(n, s)
        # print(f"segments: {segments}")
        m = len(segments) - 2  # don't count guardian
        actives = self.create_active(m, segments)
        # print(f"active: {actives}")
        if m > 0:
            rmg = RangeMinimumQuery(actives)
        maxn = int(1e5 + 5)
        res = []
        for l, r in queries:
            if m == 0:
                res.append(su[n])
                continue
            l, r = l + 1, r + 1
            index_l = bisect_right(segments, [l, l])
            index_r = bisect_left(segments, [r, r], key=lambda x: [x[1], x[0]]) - 1
            # print(f"l: {l}, r: {r}, index_l: {index_l}, index_r: {index_r}")
            if (index_l > index_r) or (not ((1 <= index_l <= m) and (1 <= index_r <= m))):
                res.append(su[n])
                continue
            left_value = (min(r, segments[index_l + 1][0] - 1) - segments[index_l][1]) + (segments[index_l][0] - max(segments[index_l - 1][1] + 1, l))
            right_value = (min(r, segments[index_r + 1][0] - 1) - segments[index_r][1]) + (segments[index_r][0] - max(segments[index_r - 1][1] + 1, l))
            ans = max(left_value, right_value)
            if index_l + 1 <= index_r - 1:
                ans = max(ans, actives[rmg.query(index_l + 1, index_r - 1)])

            res.append(su[n] + ans)
        return res
