# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        if root.left is None and root.right is None: return [root.val]

        dq = deque()
        dq.append((root, 1))
        visited = [0]*101
        ans = []

        while dq:
            node, level = dq.pop()
            if visited[level] == 0:
                visited[level] = 1
                ans.append(node.val)
            # print(level, ": ", node.val)

            if node.left: dq.append((node.left, level+1))
            if node.right: dq.append((node.right, level+1))
        
        return ans