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

        def buid_distance(u, parent_u, adj, level, max_level):
            if level > max_level:
                return
            cnt = 1
            for v in adj[u]:
                if v != parent_u:
                    cnt += build_distance(v, u, adj, level + 1, max_level)
            return cnt
        max_on_tree2 = -1
        for u in range(m):
            cnt = build_distance(u, -1, adj2, 0, k - 1)
            max_on_tree2 = max(max_on_tree2, cnt)
        res = 0
        for i in range(n):
            cnt1 = build_distance(i, -1, adj1, 0, k)
            res = max(res, cnt1 + max_on_tree2)
        return ans
