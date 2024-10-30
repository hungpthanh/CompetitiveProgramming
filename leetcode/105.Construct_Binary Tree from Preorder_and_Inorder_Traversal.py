# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0], None, None)
        root_index = inorder.index(preorder[0])
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]
        left_preorder = preorder[1: 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]
        
        return TreeNode(inorder[root_index], self.buildTree(left_preorder, left_inorder), self.buildTree(right_preorder, right_inorder))
