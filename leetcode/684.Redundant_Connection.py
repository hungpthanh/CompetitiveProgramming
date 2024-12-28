class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i: [] for i in range(1, n + 1)}
        for (u, v) in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        results = None
        def dfs(u):
            nonlocal results
            if results is not None:
                return
            for v in adj[u]:
                if v in visited:
                    if [u, v] in edges:
                        results = [u, v]
                    else:
                        results = [v, u]
                else:
                    visited.add(v)
                    dfs(v)
        visited.add(1)
        dfs(1)
