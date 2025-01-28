# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        Q = deque()
        Q.append((root, 0))
        ans = [root.val]
        while len(Q) > 0 :
            node, depth = Q.popleft()
            if depth >= len(ans):
                ans.append(node.val)
            else:
                ans[depth] = node.val
            if node.left is not None:
                Q.append((node.left, depth + 1))
            if node.right is not None:
                Q.append((node.right, depth + 1))
        return ans
