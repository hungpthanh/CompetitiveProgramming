# SOL: color graph
# Hint: u target to v then number of node target u = number of node target v
# ans[i] = even[i] + max(m - min(even2[0], ...even2[m - 1]), max(even2[0], ..., even2[m - 1])
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        def build_adj(n, edges):
            adj = {u: [] for u in range(n)}
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        adj1 = build_adj(n, edges1)
        adj2 = build_adj(m, edges2)

        def dfs(u, parent_u, adj, color):
            s = 1 if color[u] == 0 else 0
            for v in adj[u]:
                if v != parent_u:
                    color[v] = (color[u] + 1) % 2
                    s_child = dfs(v, u, adj, color)
                    s += s_child
            return s
        color1 = {i: 0 for i in range(n)}
        color2 = {i: 0 for i in range(m)}

        p1 = dfs(0, -1, adj1, color1)
        p2 = dfs(0, -1, adj2, color2)

        add = max(p2, m - p2)

        res = []
        for i in range(n):
            ans = p1 if color1[i] == 0 else n - p1
            res.append(ans + add)
        return res
        
