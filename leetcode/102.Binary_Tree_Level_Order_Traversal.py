# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        results = []
        Q = deque()
        if root is None:
            return []
        Q.append((root, 1))
        
        while (len(Q) > 0):
            front = Q.popleft()
            if len(results) < front[1]:
                results.append([])
            results[-1].append(front[0].val)
            if front[0].left is not None:
                Q.append((front[0].left, front[1] + 1))
            if front[0].right is not None:
                Q.append((front[0].right, front[1] + 1))
        return results
