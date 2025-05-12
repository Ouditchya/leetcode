# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root.left == None and root.right == None: return [root.val]

        dq = deque()
        mydict = defaultdict(list)

        dq.append((root, 0))

        while dq:
            node, level = dq.popleft()
            # print(level, ": ", node.val)
            ls = mydict.get(level, [0, 0])
            ls[0] += node.val
            ls[1] += 1
            mydict[level] = ls

            if node.left: dq.append((node.left, level+1))
            if node.right: dq.append((node.right, level+1))

        # print(mydict)
        ls = []
        for k, v in mydict.items(): ls.append(v[0]/v[1])

        return ls