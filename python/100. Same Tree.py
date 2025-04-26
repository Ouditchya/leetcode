# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(node1, node2):
            if node1 == None and node2 == None:
                return 0
            
            c1 = node1 == None and node2 is not None
            c2 = node2 == None and node1 is not None
            if c1 or c2:
                return 1
            
            c1 = node1.left == None and node2.left is not None
            c2 = node2.right == None and node1.right is not None
            if c1 or c2:
                return 1

            print(node1.val, node2.val)
            if node1.val != node2.val:
                return 1
            
            return max(traverse(node1.left, node2.left), traverse(node1.right, node2.right))


        return traverse(p, q) == 0