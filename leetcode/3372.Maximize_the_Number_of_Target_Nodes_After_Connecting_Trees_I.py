class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        def build_adj(n, edges):
            adj = {i: [] for i in range(n)}
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            return adj

        adj1 = build_adj(n, edges1)
        adj2 = build_adj(m, edges2)

        def dfs(u: int, adj, visited, distance, dis):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dis[v] = distance + 1
                    dfs(v, adj, visited, dis[v], dis)
        max_dis = [0 for _ in range(m)]
        for i in range(m):
            visited = [False for _ in range(m)]
            dis2 = [0 for _ in range(m)]
            distance = 0
            dfs(i, adj2, visited, 0, dis2)
            for j in range(m):
                if dis2[j] <= k - 1:
                    max_dis[i] += 1

        ans = []
        for i in range(n):
            res = 0
            visited = [False for _ in range(n)]
            dis1 = [0 for _ in range(n)]
            distance = 0
            dfs(i, adj1, visited, 0, dis1)
            init_cnt = 0
            for d in dis1:
                if d <= k:
                    init_cnt += 1

            res = 0
            for j in range(m):
                res = max(res, init_cnt + max_dis[j])

            ans.append(res)
        return ans
