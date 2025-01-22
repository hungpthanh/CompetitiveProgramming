class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: set() for i in range(numCourses)}
        orders = []
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
            orders.append(u)
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                res = dfs(i)
                if not res:
                    return []
        return orders[::-1]
