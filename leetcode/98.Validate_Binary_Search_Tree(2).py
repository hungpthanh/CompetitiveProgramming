# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBSTwithVar(self, root):
        min_left, min_right = 2147483649, 2147483649
        max_left, max_right = -2147483649, -2147483649
        valid_left, valid_right = True, True
        if root.left is not None:
            valid_left, min_left, max_left = self.isValidBSTwithVar(root.left)
        if root.right is not None:
            valid_right, min_right, max_right = self.isValidBSTwithVar(root.right)
        
        if valid_left and valid_right and max_left < root.val < min_right:
            return True, min(min_left, root.val), max(max_right, root.val)
        return False, 2147483649, -2147483649

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.isValidBSTwithVar(root)[0]
        
