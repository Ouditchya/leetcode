# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        if root.left == None and root.right == None: return [root.val]

        def postorderTraversal(node):
            nonlocal ls
            if node == None: return
            postorderTraversal(node.left)
            postorderTraversal(node.right)
            ls.append(node.val)

        ls = []
        postorderTraversal(root)

        return ls