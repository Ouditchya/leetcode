# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Edge Cases
        c1 = root == None or (root.left == None and root.right == None)
        c2 = root.left == None and root.right != None
        c3 = root.right == None and root.left != None
        if c1: return True
        elif c2 or c3: return False

        def bfs(node, f) -> list:
            queue = deque([node])
            result = []

            while queue:
                curr = queue.popleft()
                if curr:
                    result.append(curr.val)

                    if f == 0:  # left subtree → left to right
                        queue.append(curr.left)
                        queue.append(curr.right)
                    else:       # right subtree → right to left (mirror)
                        queue.append(curr.right)
                        queue.append(curr.left)
                else:
                    result.append(None)

            return result

        ls_l = bfs(root.left, 0)
        ls_r = bfs(root.right, 1)

        # print(ls_l)
        # print(ls_r)

        return ls_l == ls_r