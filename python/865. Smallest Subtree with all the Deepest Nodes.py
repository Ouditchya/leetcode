# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left == None and root.right == None: return root

        def traverse(node, ls):
            if node == None: 
                if ls not in paths: paths.append(ls[:])
                return 
            ls.append(node.val)
            traverse(node.left, ls)
            traverse(node.right, ls)
            ls.pop()
   
        paths = []
        traverse(root, [])
        # print(paths)

        maxlen = 0
        for ls in paths: maxlen = max(maxlen, len(ls))

        ans = []
        for ls in paths:
            if maxlen == len(ls): ans.append(ls)
        # print(ans)

        mydict = defaultdict(list)
        for ls in ans:
            for j in range(maxlen): mydict[j].append(ls[j])
        # print(mydict)

        if len(mydict[maxlen-1]) == 1: val = mydict[maxlen-1][0]
        else:
            for i in range(maxlen-2, -1, -1):
                if len(mydict[i]) == len(mydict[maxlen-1]): 
                    f = 0
                    for j in range(1, len(mydict[i])):
                        if mydict[i][j] != mydict[i][j-1]: f = 1
                    if f == 0:
                        val = mydict[i][0]
                        break
        # print(val)
        
        def find(node) -> Optional[TreeNode]:
            nonlocal val
            if node == None: return None
            if node.val == val: return node
            l = find(node.left)
            if l: return l
            r = find(node.right)
            if r: return r

        return find(root)