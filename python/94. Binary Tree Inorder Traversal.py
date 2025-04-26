# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        def inorder_traversal(node, ls) -> list:
            if node == None:
                return
            if node.left != None:
                inorder_traversal(node.left, ls)
            # print(node.val)
            ls.append(node.val)
            if node.right != None:
                inorder_traversal(node.right, ls)
            return ls
        
        def call_inorder_traversal(node) -> list:
            ls = []
            return inorder_traversal(node, ls)

        return call_inorder_traversal(root)