# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, flag = 0):
            nonlocal leftLeafSum
            if node == None: return
            if node.left == None and node.right == None and flag == 1: leftLeafSum += node.val
            traverse(node.left, 1)
            traverse(node.right)

        leftLeafSum = 0
        traverse(root)
        
        return leftLeafSum