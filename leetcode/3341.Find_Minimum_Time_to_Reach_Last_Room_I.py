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
        d = [MAX_VAL for _ in range(p + 1)]
        P = [False for _ in range(p + 1)]
        d[1] = 0
        for i in range(1, p + 1):
            max_u = p + 1
            for j in range(1, p + 1):
                if (((max_u != p + 1) and (d[max_u] > d[j]) ) or (max_u == p + 1)) and not P[j]:
                    max_u = j
            
            u, v = index2xy(n, m, max_u)
            P[max_u] = True
            cx = [-1, 1, 0, 0]
            cy = [0, 0, -1, 1]
            for k in range(4):
                nu = u + cx[k]
                nv = v + cy[k]
                if (1 <= nu <= n) and (1 <= nv <= m):
                    new_dis = d[max_u] + 1 + (moveTime[nu - 1][nv - 1] - d[max_u] if moveTime[nu - 1][nv - 1] >= d[max_u] else 0)
                    d[(nu - 1)* m + nv] = min(d[(nu - 1) * m + nv], new_dis)
        return d[p]
