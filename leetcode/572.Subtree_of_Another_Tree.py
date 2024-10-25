# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if (p is None) and (q is None):
            return True
        if (p is None) or (q is None):
            return False
        if (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False
        
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if root.val == subRoot.val:
            sameTree = self.isSameTree(root, subRoot)
            if sameTree:
                return True
        
        if root.left is not None:
            if self.isSubtree(root.left, subRoot):
                return True
        if root.right is not None:
            if self.isSubtree(root.right, subRoot):
                return True
        return False
        
