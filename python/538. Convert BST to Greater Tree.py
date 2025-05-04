# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return None

        def reverseInOrder(node):
            nonlocal runningSum
            if node == None: return
            reverseInOrder(node.right)
            runningSum += node.val
            node.val = runningSum
            reverseInOrder(node.left)
            
        runningSum = 0
        reverseInOrder(root)

        return root