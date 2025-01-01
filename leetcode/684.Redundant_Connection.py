# IN MEMORY OF MY GRANDMOTHER 2025/01/01
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [-1] * (n + 1)  # Union-Find data structure to track sets

        def find(v: int) -> int:
            """Finds the representative (root) of the set containing `v`."""
            if parent[v] < 0:
                return v
            parent[v] = find(parent[v])  # Path compression
            return parent[v]

        def union(u: int, v: int) -> bool:
            """Unites the sets containing `u` and `v`. Returns `False` if they are already connected."""
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                # Union by size: attach the smaller tree under the larger tree
                if parent[root_u] > parent[root_v]:
                    root_u, root_v = root_v, root_u
                parent[root_u] += parent[root_v]
                parent[root_v] = root_u
                return True
            return False

        # Process each edge in the graph
        for u, v in edges:
            if not union(u, v):  # If union fails, the edge is redundant
                return [u, v]

        return []  # Default return (should not reach here in a valid input)
