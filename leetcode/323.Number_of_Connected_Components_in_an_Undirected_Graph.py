class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(u: int) -> None:
            nonlocal visited
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    dfs(v)
        adj = [[] for u in range(n)]
        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        cnt = 0
        for u in range(n):
            if u in visited:
                continue
            cnt += 1
            visited.add(u)
            dfs(u)
        return cnt
