# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if root.left == None and root.right == None: return 1

        def traverse(node):
            if node == None: return (0, 0)
            if node.left == None and node.right == None: 
                ans.append(node.val)
                return (node.val, 1)
            lval, ln = traverse(node.left)
            rval, rn = traverse(node.right)
            n = ln + rn + 1
            rSum = lval + rval + node.val
            avg = rSum// n
            if node.val == avg: ans.append(node.val)
            # print("node.val: ", node.val, " n: ", n, " rSum: ", rSum, " avg: ", avg)
            return (rSum, n)

        ans = []
        traverse(root)

        return len(ans)