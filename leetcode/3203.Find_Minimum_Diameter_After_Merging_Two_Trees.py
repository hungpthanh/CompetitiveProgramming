# IDEA: TBD
# Resource: https://codeforces.com/blog/entry/101271
# TODO: Improve the final equation
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n, m = len(edges1) + 1, len(edges2) + 1
        def build(n, edges):
            adj = {i: [] for i in range(n)}
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj
        adj1 = build(n, edges1)
        adj2 = build(m, edges2)

        def dfs(u, parent_u, n, dis, distances, adj):
            for v in adj[u]:
                if v != parent_u:
                    distances[v] = dis + 1
                    dfs(v, u, n, dis + 1, distances, adj)
        
        def argmax(my_list):
            max_value = max(my_list)
            argmax_index = my_list.index(max_value)
            return argmax_index

        def return_max_distance_nodes(n, adj):
            
            distance = [0] * n
            dfs(0, -1, n, 0, distance, adj)
            a = argmax(distance)

            distance_a = [0] * n
            dfs(a, -1, n, 0, distance_a, adj)
            b = argmax(distance_a)

            distance_b = [0] * n
            dfs(b, -1, n, 0, distance_b, adj)
            
            distance = [max(distance_a[i], distance_b[i]) for i in range(n)]

            return distance

        distance1 = return_max_distance_nodes(n, adj1)
        distance2 = return_max_distance_nodes(m, adj2)

        min_1 = min(distance1)
        min_2 = min(distance2)

        res = max(min_1 + min_2 + 1, max(distance1), max(distance2))

        return res
        
