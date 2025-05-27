# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None: return 1

        dq = deque()
        dq.append((root, 1))
        levelSum = [0] * 10001
        levelMax = 1

        while dq:
            node, level = dq.pop()
            levelSum[level] += node.val
            levelMax = max(levelMax, level)

            if node.left: dq.append((node.left, level+1))
            if node.right: dq.append((node.right, level+1))
        
        # print(levelMax, levelSum[1:levelMax+1])
        maxVal = max(levelSum[1:levelMax+1])
        for level in range(1, levelMax+1):
            if levelSum[level] == maxVal: break

        return level