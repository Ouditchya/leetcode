# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None: return root.val
        
        dq = deque()
        mydict = defaultdict(list)
        max_lvl = 0

        dq.append((root, 1))
        while dq:
            node, lvl = dq.popleft()
            max_lvl = max(max_lvl, lvl)
            mydict[lvl].append(node.val)

            if node.left != None: dq.append((node.left, lvl+1))
            if node.right != None: dq.append((node.right, lvl+1))

        return sum(mydict[max_lvl])