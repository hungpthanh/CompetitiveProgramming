class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cx = [-1, 1, 0, 0]
        cy = [0, 0, -1, 1]
        Q = deque()
        m, n = len(grid), len(grid[0])
        t = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    Q.append(((i, j), 0))
                if grid[i][j] == 1:
                    t[(i, j)] = -1
        while len(Q) > 0:
            top = Q.popleft()
            x, y = top[0]
            ct = top[1]
            for k in range(4):
                nx = x + cx[k]
                ny = y + cy[k]
                if (0 <= nx < m) and (0 <= ny < n) and grid[nx][ny] == 1:
                    Q.append(((nx, ny), ct + 1))
                    t[(nx, ny)] = ct + 1
                    grid[nx][ny] = -1
        maxt = 0
        for k, v in t.items():
            if v == -1:
                return -1
            maxt = max(maxt, v)
        return maxt
            
