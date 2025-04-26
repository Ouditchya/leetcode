# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge Case 1
        if head.next == None and n == 1:
            return None
        p1, p2, ctr = head, head, 0
        while ctr < n:
            ctr += 1
            p1 = p1.next

        # Edge Case 2
        if p1 == None:
            return head.next

        while p1 != None:
            if p1.next == None:
                break
            p1 = p1.next
            p2 = p2.next
        p3 = p2.next.next
        p2.next = p3
        return head