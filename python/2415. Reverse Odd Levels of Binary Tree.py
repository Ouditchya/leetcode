# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left == None and root.right == None: return root

        arr, dq = [], deque()
        dq.append((root, 1))

        while dq:
            node, lvl = dq.popleft()

            if lvl % 2 == 0:
                new_val = arr.pop()
                node.val = new_val

            if node.left != None: 
                dq.append((node.left, lvl+1))
                if lvl % 2 != 0: arr.append(node.left.val)
            if node.right != None: 
                dq.append((node.right, lvl+1))
                if lvl % 2 != 0: arr.append(node.right.val)

        return root