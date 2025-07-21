# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None: return root2
        if root2 is None: return root1

        root3 = TreeNode()
        root3.val = root1.val + root2.val
        
        dq = deque()
        dq.append((root3, root1.left, root2.left, 1))
        dq.append((root3, root1.right, root2.right, 2))

        while dq:
            parent, r1, r2, side = dq.popleft()
            child = TreeNode()

            if r1 is None and r2 is None: continue
            elif r1 is None: 
                child.val = r2.val
                dq.append((child, None, r2.left, 1))
                dq.append((child, None, r2.right, 2))
            elif r2 is None: 
                child.val = r1.val
                dq.append((child, r1.left, None, 1))
                dq.append((child, r1.right, None, 2))
            else: 
                child.val = r1.val + r2.val
                dq.append((child, r1.left, r2.left, 1))
                dq.append((child, r1.right, r2.right, 2))

            if side == 1: parent.left = child
            else: parent.right = child

        return root3