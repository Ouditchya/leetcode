# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0
        p1, p2 = l1, l2
        dq1, dq2 = deque(), deque()

        while p1 != None:
            n1 += 1
            dq1.append(p1.val)
            p1 = p1.next
        while p2 != None:
            n2 += 1
            dq2.append(p2.val)
            p2 = p2.next
        # print(n1, n2)

        if n1 >= n2: r1, r2 = dq1, dq2
        else: r1, r2 = dq2, dq1

        itr, c = 0, 0
        while r1:
            v1 = r1.pop()
            if r2: v2 = r2.pop()
            else: v2 = 0
            
            v = (v1 + v2 + c) % 10
            c = 1 if (v1 + v2 + c) > 9 else 0
            p0 = ListNode(v)
            # print(v1, v2, v, c, p0)
            if itr == 0:
                tail = p0
            else:
                p0.next = tail
                tail = p0
            itr += 1

        if c == 1:
            p0 = ListNode(1)
            p0.next = tail
            tail = p0

        return tail