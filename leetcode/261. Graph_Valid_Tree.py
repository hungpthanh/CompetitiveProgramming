class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = [[] for u in range(n)]
        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)

        mark = set()
        def dfs(parent: int, u: int) -> None:
            for v in adj[u]:
                if (v != parent):
                    if v in mark:
                        return False
                    mark.add(v)
                    return dfs(u, v)
            return True
        return dfs(-1, 0)
