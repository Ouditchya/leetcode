# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, s):
            if not node.left and not node.right: 
                arr.append(s+str(node.val))
                return

            if node.left: dfs(node.left, s+str(node.val))
            if node.right: dfs(node.right, s+str(node.val))

        def binaryToDecimal(s):
            num, base = 0, 1
            for c in s[::-1]:
                num += base * int(c)
                base <<= 1
            return num
        
        arr = []
        dfs(root, '')
        
        ans = 0
        for s in arr: ans += binaryToDecimal(s)

        return ans