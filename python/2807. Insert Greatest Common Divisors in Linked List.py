# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return head

        p0, p1 = head, head.next
        while p1:
            p2 = ListNode(math.gcd(p0.val, p1.val))
            p0.next = p2
            p2.next = p1
            p0 = p1
            p1 = p1.next
        
        return head      