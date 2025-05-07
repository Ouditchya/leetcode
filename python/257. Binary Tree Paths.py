# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left == None and root.right == None: return [str(root.val)]
        
        paths, strpaths = [], []

        def traverse(node):
            if node == None: return
            print(node.val, end = " ")
            traverse(node.left)
            traverse(node.right)
        
        # traverse(root)

        def generatePaths(node, ls):
            if node == None: return
            ls.append(node.val)
            # print("Visited: ", node.val, " ls: ", ls)
            if node.left == None and node.right == None: 
                paths.append(ls[:])
                ls.pop()
                # print("path: ", path)
                return 
            generatePaths(node.left, ls)
            generatePaths(node.right, ls)
            ls.pop()

        generatePaths(root, [])
        # print(paths)

        for path in paths:
            str1 = str(path[0])
            for i in range(1, len(path)): str1 += ("->" + str(path[i]))
            strpaths.append(str1)

        return strpaths