# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p0, p1 = head, head.next
        rSum, ls = 0, []
        while p1:
            if p1.val == 0:
                ls.append(rSum)
                rSum = 0
                p0 = p1
            else:
                rSum += p1.val
            p1 = p1.next
        
        newHead = ListNode(ls[0])
        n, p1 = len(ls), newHead
        for i in range(1, n):
            node = ListNode(ls[i])
            p1.next = node
            p1 = p1.next

        return newHead