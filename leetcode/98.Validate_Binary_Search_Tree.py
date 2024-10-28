# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBSTrange(self, root, min_x, max_x):
        if root is None:
            return True
        if (min_x <= root.val <= max_x):
             return self.isValidBSTrange(root.left, min_x, root.val - 1) and self.isValidBSTrange(root.right, root.val + 1, max_x)
        return False

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isValidBSTrange(root, -2147483648, 2147483648 - 1)
        
