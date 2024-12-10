class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        cx = [0, 1, 0, -1]
        cy = [1, 0, -1, 0]
        results = []
        cnt = 0
        def move(i, j, direction):
            nonlocal cnt
            x = i + cx[direction]
            y = j + cy[direction]
            if (0 <= x < n) and (0 <= y < m) and matrix[x][y] != -101:
                cnt = 0
                results.append(matrix[i][j])
                matrix[i][j] = -101
                move(x, y, direction)
            else:
                direction = (direction + 1) % 4
                cnt += 1
                if cnt == 4:
                    results.append(matrix[i][j])
                    return
                move(i, j, direction)
        
        move(0, 0, 0)
        return results
            
