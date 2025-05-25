# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, currSum, level):
            nonlocal paths
            
            # Boundary Condition
            if node is None: return

            # Visit node
            currSum += node.val
            # print("node.val: ", node.val, " currSum: ", currSum, " level: ", level, " paths: ", paths)

            # if currSum exceeds targetSum reset currSum
            # if currSum > targetSum: currSum = node.val if node.val <= targetSum else 0
            
            # if currSum equals targetSum reset currSum, increment path count and reset currSum
            if currSum == targetSum: 
                # currSum = node.val if node.val <= targetSum else 0
                paths = paths+1

            # Traversal
            # print("currSum: ", currSum, " paths: ", paths)
            dfs(node.left, currSum, level+1)
            dfs(node.right, currSum, level+1)
            # print("-----------------------------------------------------------")

        def dfs_all(node):
            if node is None: return
            dfs(node, 0, 1)
            dfs_all(node.left)
            dfs_all(node.right)

        paths = 0
        dfs_all(root)        

        return paths