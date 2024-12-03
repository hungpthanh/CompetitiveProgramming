class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: set() for i in range(numCourses)}
        for [a, b] in prerequisites:
            adj[b].add(a)
        visited = [0] * numCourses
        def dfs(u) -> bool:
            visited[u] = 1
            for v in adj[u]:
                if visited[v] == 1:
                    return False
                elif visited[v] == 0:
                    res = dfs(v)
                    if not res:
                        return False
            visited[u] = 2
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                res = dfs(i)
                if not res:
                    return False
        return True
        
