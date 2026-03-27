# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def calculate(node,parent,grandparent):
            if not node:
                return 0
            total = 0
            if grandparent and grandparent.val % 2 == 0:
                total += node.val
            total += calculate(node.left,node,parent)
            total += calculate(node.right,node,parent)
            
            return total
        return calculate(root,None,None)


