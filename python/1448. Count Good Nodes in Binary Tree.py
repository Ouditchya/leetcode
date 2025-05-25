# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if root.left is None and root.right is None: return 1

        def dfs(node, currMax, level):
            nonlocal n_good

            if node is None: return

            if node.val >= currMax:
                n_good += 1
                currMax = node.val
                # print(level, ": node.val = ", node.val, " currMax = ", currMax, " n_good = ", n_good) 
            
            dfs(node.left, currMax, level+1)
            dfs(node.right, currMax, level+1)
            # print("-------------------------------------------------")

        n_good = 0
        dfs(root, root.val, 1)

        return n_good