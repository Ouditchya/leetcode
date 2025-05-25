# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, target, ls):
            nonlocal flag, ans
            if node is None or flag: return
            
            ls.append(node.val)
            
            if node.val == target.val:
                ans = ls[:]    
                flag = True
                return
            # print(node.val)
            dfs(node.left, target, ls)
            dfs(node.right, target, ls)
            ls.pop()

        flag, ans = False, []
        dfs(root, p, [])
        pArr = ans.copy()
        
        flag, ans = False, []
        dfs(root, q, [])
        qArr = ans.copy()

        # print(pArr)
        # print(qArr)

        lcaVal, lp, lq = 10**9+1, len(pArr), len(qArr)
        for i in range(lp-1, -1, -1):
            for j in range(lq-1, -1, -1):
                if pArr[i] == qArr[j]:
                    lcaVal = pArr[i]
                    break
            if lcaVal == pArr[i]: break
        # print("lcaVal: ", lcaVal)
        
        def getLCANode(node, lcaVal):
            nonlocal flag, ansNode
            if node is None or flag: return
            if node.val == lcaVal: 
                ansNode = node
                flag = True
                return
            getLCANode(node.left, lcaVal)
            getLCANode(node.right, lcaVal)

        flag, ansNode = False, TreeNode()
        getLCANode(root, lcaVal)
        # print("ansNode: ", ansNode)

        return ansNode