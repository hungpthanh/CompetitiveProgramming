class State:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        inf = float("inf")
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        d = [[inf] * m for _ in range(n)]
        v = [[0] * m for _ in range(n)]
        d[0][0] = 0
        q = []
        heapq.heappush(q, State(0, 0, 0))

        while q:
            s = heapq.heappop(q)
            v[s.x][s.y] = 1
            if s.x == n -1 and s.y == m - 1:
                return s.dis
            for cx, cy in dirs:
                nx, ny = s.x + cx, s.y + cy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if v[nx][ny]:
                    continue
                
                dist = max(d[s.x][s.y], moveTime[nx][ny]) + 1 + (s.x + s.y) % 2
                if dist < d[nx][ny]:
                    d[nx][ny] = dist
                    heapq.heappush(q, State(nx, ny, dist))
        return -1
        
# class Solution:
#     def minTimeToReach(self, moveTime: List[List[int]]) -> int:
#         MAX_VAL = int(1e18)
#         def index2xy(n, m, index_value):
#             index_value -= 1
#             x = (index_value) // m  + 1
#             y = (index_value) % m + 1
#             return x, y
#         n, m = len(moveTime), len(moveTime[0])
#         p = n * m
#         d = [[MAX_VAL, MAX_VAL] for _ in range(p + 1)]
#         P = [[False, False] for _ in range(p + 1)]
#         d[1][0] = 0 # 0 -1: 1 second, 1 -> 0: 2 second
#         for i in range(1, p + 1):
#             for k in range(2):
#                 max_u = (p + 1, 0)
#                 for j in range(1, p + 1):
#                     for k2 in range(2):
#                         if ((max_u != (p + 1, 0) and (d[max_u[0]][max_u[1]] > d[j][k2])) or (max_u == (p + 1, 0))) and not P[j][k2]:
#                             max_u = (j, k2)
                
#                 u, v = index2xy(n, m, max_u[0])
#                 P[max_u[0]][max_u[1]] = True
#                 cx = [-1, 1, 0, 0]
#                 cy = [0, 0, -1, 1]
#                 for k in range(4):
#                     nu = u + cx[k]
#                     nv = v + cy[k]
#                     if (1 <= nu <= n) and (1 <= nv <= m):
#                         new_dis = d[max_u[0]][max_u[1]] + (1 if max_u[1] == 0 else 2) + (moveTime[nu - 1][nv - 1] - d[max_u[0]][max_u[1]] if moveTime[nu - 1][nv - 1] >= d[max_u[0]][max_u[1]] else 0)
#                         d[(nu - 1)* m + nv][1 - max_u[1]] = min(d[(nu - 1) * m + nv][1 - max_u[1]], new_dis)
#         return min(d[p])
