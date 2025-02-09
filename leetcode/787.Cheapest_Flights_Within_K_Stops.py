class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k += 1
        adj = {i: [] for i in range(n)}
        for u, v, p in flights:
            adj[u].append((v, p))
        INF = 1e9 + 5
        D = [[INF for t in range(k + 1)] for _ in range(n)]
        P = [[False for t in range(k + 1)] for _ in range(n)]

        D[src][0] = 0
        
        for i in range(n * k):
            Max = INF
            uBest = None
            for u in range(n):
                for kk in range(k):
                    if (D[u][kk] < Max) and (not P[u][kk]):
                        uBest = (u, kk)
                        Max = D[u][kk]
            if uBest is None:
                break
            u, kk = uBest
            P[u][kk] = True
            for v, p in adj[u]:
                D[v][kk + 1] = min(D[v][kk + 1], D[u][kk] + p)
        res = min(D[dst])
        return res if res < INF else -1
        
