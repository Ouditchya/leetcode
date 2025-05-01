# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None: return False
        elif root.left == None and root.right == None: 
            if root.val == targetSum: return True
            else: return False
        
        queue = deque([(root, root.val)])

        while queue:
            node, currSum = queue.popleft()

            # print(node.val, currSum)

            if node.left == None and node.right == None:
                if currSum == targetSum:
                    return True
            
            if node.left: queue.append((node.left, currSum + node.left.val))
            if node.right: queue.append((node.right, currSum + node.right.val))
        
        return False