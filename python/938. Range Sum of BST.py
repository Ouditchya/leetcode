# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def traverse(node):
            if node == None: return
            if node.val >= low and node.val <= high: myset.add(node.val)

            if node.val > high: traverse(node.left)
            elif node.val < low: traverse(node.right)
            else:
                traverse(node.left)
                traverse(node.right)
                
            return myset

        myset = set()
        traverse(root)
        ls = [x for x in myset]
        
        return sum(ls)