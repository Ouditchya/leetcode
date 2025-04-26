# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node):
            if node == None:
                return
            l_node, r_node = node.left, node.right
            node.left, node.right = r_node, l_node
            # print(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return root