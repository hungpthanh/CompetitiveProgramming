# IDEA: TBD
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent = [-1 for _ in range(n)]
        
        childs = [[] for _ in range(n)]
        def build_tree(u, level):
            for v in adj[u]:
                if v != 0 and parent[v] == -1:
                    parent[v] = (u, level + 1)
                    childs[u].append(v)
                    build_tree(v, level + 1)
        level = 0
        t = [-1 for _ in range(n)]
        while parent[bob] != -1:
            t[bob] = level
            level += 1
            bob = parent[bob]
        
        dp = [0 for _ in range(n)]
        mark = [False for _ in range(n)]
        def dfs(u):
            mark[u] = True
            for v in childs[u]:
                if not mark[v]:
                    dp[v] = dp[u] + amount[v] if (parent[v][1] != t[v]) else amount[v] / 2
                    dfs(v)
        dfs(0)
        ans = -1e18
        for u in range(n):
            if len(childs[u]) == 0:
                ans = max(ans, dp[u])
        return ans





        
        
