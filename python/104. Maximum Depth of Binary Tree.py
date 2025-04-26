# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0

        def traverse(node, num) -> int:
            if node == None:
                return num
            # print("Node: ", node.val, " Level: ", num)
            # traverse(node.left, num+1)
            # traverse(node.right, num+1)
            return max(traverse(node.left, num+1), traverse(node.right, num+1))

        max_num = traverse(root, 0)

        return max_num