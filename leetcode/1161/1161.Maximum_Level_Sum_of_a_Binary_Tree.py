# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        Q = deque([(root, 1)])
        cnt = {}
        while len(Q) > 0:
            node, level = Q.popleft()
            if level not in cnt:
                cnt[level] = 0
            cnt[level] = cnt[level] + node.val
            if node.left is not None:
                Q.append((node.left, level + 1))
            if node.right is not None:
                Q.append((node.right, level + 1))
        save_value = int(-1e10)
        save_level = -1
        for key, value in cnt.items():
            if value > save_value:
                save_value = value
                save_level = key
            elif value == save_value:
                save_level = min(save_level, key)
        return save_level
            
        
            