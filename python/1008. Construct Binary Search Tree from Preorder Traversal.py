# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n, root = len(preorder), TreeNode(preorder[0])
        if n == 1: return root

        def buildBST(node, val):
            nonlocal f
            if node == None: return
            # print("visited: ", node.val)
            if val < node.val: buildBST(node.left, val)
            elif val > node.val: buildBST(node.right, val)
            
            new_node = TreeNode(val)

            if val < node.val and f == 0: 
                # print("insert left: ", val, node.val)
                node.left = new_node
                f = 1
            elif val > node.val and f == 0: 
                # print("insert right: ", val, node.val)
                node.right = new_node
                f = 1
            # print("-------------------------------------------")

        def traverse(node):
            if node == None: return
            traverse(node.left)
            print(node.val, end = " ")
            traverse(node.right)

        for i in range(1, n): 
            f = 0
            buildBST(root, preorder[i])

        # traverse(root)

        return root