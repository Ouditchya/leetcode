# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def traversal(node, minVal, maxVal):
            nonlocal ls
            if node == None: return [1000000, -1000000]
            lb1, ub1 = traversal(node.left, minVal, maxVal)
            lb2, ub2 = traversal(node.right, minVal, maxVal)
            # print("1: ", lb1, ub1, "\n2: ", lb2, ub2)
            if node.left:
                minVal = min(minVal, lb1, lb2, node.left.val)
                maxVal = max(maxVal, ub1, ub2, node.left.val)
            if node.right:
                minVal = min(minVal, lb1, lb2, node.right.val)
                maxVal = max(maxVal, ub1, ub2, node.right.val)
            # print(node.val, minVal, maxVal, "\n-------------------------")
            if minVal != 1000000: ls.append(abs(node.val - minVal))
            if maxVal != -1000000: ls.append(abs(node.val - maxVal))
            return [minVal, maxVal]

        ls = []
        traversal(root, 1000000, -1000000)
        ls.sort()
        # print(ls)

        return ls[-1]