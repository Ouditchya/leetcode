# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None: return 0

        req_sum = 0
        dq = deque()

        dq.append((root, None, None))
        while dq:
            node, parent, grandparent = dq.popleft()

            if grandparent and grandparent.val % 2 == 0: req_sum += node.val
            
            if node.left != None: dq.append((node.left, node, parent))
            if node.right != None: dq.append((node.right, node, parent))

        return req_sum