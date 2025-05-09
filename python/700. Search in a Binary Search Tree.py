# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def traverseBST(node):
            nonlocal ansNode
            if node == None: return
            # print(node.val, end = " > ")
            if val == node.val: 
                ansNode = node
                return
            elif val > node.val: traverseBST(node.right)
            else: traverseBST(node.left)
        
        ansNode = None
        traverseBST(root)

        return ansNode