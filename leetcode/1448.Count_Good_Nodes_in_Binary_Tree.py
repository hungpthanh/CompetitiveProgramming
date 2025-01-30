# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def f(u: TreeNode, max_parent: int):
            nonlocal ans
            if u is None:
                return
            if max_parent <= u.val:
                ans += 1
            max_parent = max(max_parent, u.val)
            f(u.left, max_parent)
            f(u.right, max_parent)
        f(root, -2 * 1e4)
        return ans
