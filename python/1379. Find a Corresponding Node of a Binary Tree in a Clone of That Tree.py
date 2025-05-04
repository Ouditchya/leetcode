# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def traverse(node):
            nonlocal clonedNode
            if node == None: return
            # print("Visited: ", node.val)
            if node.val == target.val: 
                clonedNode = node
                return

            traverse(node.left)
            traverse(node.right)

        clonedNode = None
        traverse(cloned)

        return clonedNode