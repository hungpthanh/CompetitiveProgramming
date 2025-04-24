# IDEA: TBD
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [(-1, 0) for _ in range(n)]
        
        childs = [[] for _ in range(n)]
        def build_tree(u, level):
            for v in adj[u]:
                if v != 0 and parent[v][0] == -1:
                    parent[v] = (u, level + 1)
                    childs[u].append(v)
                    build_tree(v, level + 1)
        build_tree(0, 0)
            
        level = 0
        t = [-1 for _ in range(n)]
        while parent[bob][0] != -1:
            t[bob] = level
            level += 1
            bob = parent[bob][0]
        
        dp = [0 for _ in range(n)]
        dp[0] = amount[0] if t[0] != 0 else amount[0] // 2
        def dfs(u):
            for v in childs[u]:
                if t[v] != -1:
                    if t[v] == parent[v][1]:
                        dp[v] = dp[u] + amount[v] // 2
                    elif parent[v][1] > t[v]:
                        dp[v] = dp[u]
                    else:
                        dp[v] = dp[u] + amount[v]
                else:
                    dp[v] = dp[u] + amount[v]
                dfs(v)
        dfs(0)
        ans = -1e18
        for u in range(n):
            if len(childs[u]) == 0:
                ans = max(ans, dp[u])
        return ans




        
        
