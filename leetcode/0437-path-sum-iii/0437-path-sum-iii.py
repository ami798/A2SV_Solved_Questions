# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
       
        if not root:
            return 0

        
        return (self.countFromNode(root, targetSum) +
                self.pathSum(root.left, targetSum) +
                self.pathSum(root.right, targetSum))

    def countFromNode(self, node, target):
        if not node:
            return 0

        res = 1 if node.val == target else 0

        res += self.countFromNode(node.left, target - node.val)
        res += self.countFromNode(node.right, target - node.val)

        return res
        
        