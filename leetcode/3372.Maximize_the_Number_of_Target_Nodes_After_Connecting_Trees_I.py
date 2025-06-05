class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1

        def build_adj(n, edges):
            adj = {i: [] for i in range(n)}
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            return adj

        adj1 = build_adj(n, edges1)
        adj2 = build_adj(m, edges2)

        def build_distance(u, parent_u, adj, level, max_level):
            if level > max_level:
                return 0
            cnt = 1
            for v in adj[u]:
                if v != parent_u:
                    cnt += build_distance(v, u, adj, level + 1, max_level)
            return cnt

        max_on_tree2 = max([build_distance(u, -1, adj2, 0, k - 1) for u in range(m)])
        ans = [build_distance(i, -1, adj1, 0, k) + max_on_tree2 for i in range(n)]
        return ans
