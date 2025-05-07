# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        def traverse(node, ls) -> List[int]:
            if node == None: return
            traverse(node.left, ls)
            ls.append(node.val)
            traverse(node.right, ls)
            return ls[:]

        if root1 == None: ls1 = []
        else: ls1 = traverse(root1, [])
        
        if root2 == None: ls2 = []
        else: ls2 = traverse(root2, [])

        ls1.extend(ls2)
        ls1.sort()

        return ls1