# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        Q = deque([root])
        current_level = 1
        save_sum = int(-1e10)
        while len(Q) > 0:
            l = len(Q)
            s = 0
            next_level = []
            for _ in range(l):
                node = Q.popleft()
                s += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if s > save_sum:
                save_sum, save_level = s, current_level
            current_level += 1
            Q = deque(next_level)
        return save_level