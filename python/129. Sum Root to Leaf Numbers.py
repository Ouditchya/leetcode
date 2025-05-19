# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def generateNumber(arr):
            num, n = arr[0], len(arr)
            for i in range(1, n):
                num = num*10 + arr[i]
            return num
        
        def traverse(node):
            # if node == None: return
            ls.append(node.val)
            if node.left == None and node.right == None:
                # print(ls)
                num = generateNumber(ls)
                myset.append(num)
                ls.pop()
                return
            
            # print(node.val, end = " ")
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
            ls.pop()
        
        myset, ls = [], []
        traverse(root)

        return sum([x for x in myset])