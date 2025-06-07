# SOL: color graph
# Hint: u target to v then number of node target u = number of node target v
# ans[i] = even[i] + max(m - min(even2[0], ...even2[m - 1]), max(even2[0], ..., even2[m - 1])
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        
