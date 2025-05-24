class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        MAX_VAL = int(1e18)
        def index2xy(n, m, index_value):
            index_value -= 1
            x = (index_value) // m  + 1
            y = (index_value) % m + 1
            return x, y
        n, m = len(moveTime), len(moveTime[0])
        p = n * m
        d = [[MAX_VAL, MAX_VAL] for _ in range(p + 1)]
        P = [[False, False] for _ in range(p + 1)]
        d[1][0] = 0 # 0 -1: 1 second, 1 -> 0: 2 second
        for i in range(1, p + 1):
            for k in range(2):
                max_u = (p + 1, 0)
                for j in range(1, p + 1):
                    for k2 in range(2):
                        if ((max_u != (p + 1, 0) and (d[max_u[0]][max_u[1]] > d[j][k2])) or (max_u == (p + 1, 0))) and not P[j][k2]:
                            max_u = (j, k2)
                
                u, v = index2xy(n, m, max_u[0])
                P[max_u[0]][max_u[1]] = True
                cx = [-1, 1, 0, 0]
                cy = [0, 0, -1, 1]
                for k in range(4):
                    nu = u + cx[k]
                    nv = v + cy[k]
                    if (1 <= nu <= n) and (1 <= nv <= m):
                        new_dis = d[max_u[0]][max_u[1]] + (1 if max_u[1] == 0 else 2) + (moveTime[nu - 1][nv - 1] - d[max_u[0]][max_u[1]] if moveTime[nu - 1][nv - 1] >= d[max_u[0]][max_u[1]] else 0)
                        d[(nu - 1)* m + nv][1 - max_u[1]] = min(d[(nu - 1) * m + nv][1 - max_u[1]], new_dis)
        return min(d[p])
