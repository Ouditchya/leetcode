# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left and not root.right: 
            root.val = 0
            return root

        levelMax, levelSum = 1, [0]*100001
        dq = deque()
        
        dq.append((root, 1))
        while dq:
            node, level = dq.popleft()
            levelMax = max(levelMax, level)
            levelSum[level] += node.val

            if node.left: dq.append((node.left, level+1))
            if node.right: dq.append((node.right, level+1))
        # print(levelMax, levelSum[1:levelMax+1])

        dq.append((root, 1))
        while dq:
            node, level = dq.popleft()
            if level > levelMax: break

            if level <= 2: node.val = 0

            if level >= 2 and level < levelMax:
                temp = 0
                if node.left: temp += node.left.val 
                if node.right: temp += node.right.val

                if node.left: node.left.val = levelSum[level+1] - temp
                if node.right: node.right.val = levelSum[level+1] - temp
            
            if node.left: dq.append((node.left, level+1))
            if node.right: dq.append((node.right, level+1))

        return root