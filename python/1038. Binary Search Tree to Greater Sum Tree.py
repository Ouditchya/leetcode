# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverseBST(node):
            if node == None: return
            ls.append(node.val)
            traverseBST(node.left)
            traverseBST(node.right)

        def updateBST(node):
            if node == None: return
            node.val = mydict.get(node.val, node.val)
            updateBST(node.left)
            updateBST(node.right)
        
        ls = []
        traverseBST(root)
        
        ls.sort(reverse = True)
        # print(ls)
        n = len(ls)
        ls2, mydict = [ls[0]], {ls[0]: ls[0]}
        for i in range(1, n): 
            ls2.append(ls2[i-1] + ls[i])
            mydict[ls[i]] = ls2[i]
        # print(ls2)
        # print(mydict)

        updateBST(root)

        return root