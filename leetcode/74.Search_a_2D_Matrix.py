class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def numberTo2D(index: int, m: int, n: int):
            if index % n == 0:
                return index // n - 1, n - 1
            return index // n, index % n - 1
        m, n = len(matrix), len(matrix[0])
        k = m * n
        l, r = 1, k
        while (l <= r):
            mid = (l + r) // 2
            i, j = numberTo2D(mid, m, n)
            if matrix[i][j] == target:
                return True
            if target < matrix[i][j]:
                r = mid - 1
            else:
                l = mid + 1
        return False
