# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        if root.left == None and root.right == None: return [[root.val]]

        dq = deque()
        mydict = defaultdict(list)
        dq.append((root, 1))

        while dq:
            node, lvl = dq.popleft()
            mydict[lvl].append(node.val)
            # print(lvl, ": ", node.val, end = " ")

            if node.left != None: dq.append((node.left, lvl+1))
            if node.right != None: dq.append((node.right, lvl+1))
        
        ans = []
        for v in mydict.values(): ans.append(v)

        return ans