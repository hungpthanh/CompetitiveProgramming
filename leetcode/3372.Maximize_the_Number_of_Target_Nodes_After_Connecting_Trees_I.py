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
            cnt = [0 for i in range(m)]
            for i in range(m):
                cnt[dis2[i]] += 1
            for i in range(m):
                max_dis[i] = max(max_dis[i], cnt[i])
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
            min_dis = min(dis1)
            for j in range(k - min_dis):
                res = max(res, max_dis[j] + init_cnt)
            ans.append(res)
        return ans
