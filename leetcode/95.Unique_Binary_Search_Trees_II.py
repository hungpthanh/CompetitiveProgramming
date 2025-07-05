# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gen_range(a, b):
            if a > b:
                return [None]
            if a == b:
                return [TreeNode(a, None, None)]
            res = []
            for v in range(a, b + 1):
                left = gen_range(a, v - 1)
                right = gen_range(v + 1, b)
                for l in left:
                    for r in right:
                        node = TreeNode(v, l, r)
                        res.append(node)
            return res
        return gen_range(1, n)
