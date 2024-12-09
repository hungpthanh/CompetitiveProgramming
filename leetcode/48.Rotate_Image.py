class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l, r = 0, n - 1
        while l < r:
            for i in range(r - l):
                matrix[l][l + i], matrix[l + i][r], matrix[r][r - i], matrix[r - i][l] = matrix[r - i][l], matrix[l][l + i], matrix[l + i][r], matrix[r][r - i]
            l += 1
            r -= 1
        
