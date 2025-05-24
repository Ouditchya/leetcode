# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None: return head
        
        head2 = head.next
        p1, p2 = head, head2

        while p1 and p2:
            # print(p1.val, p2.val)
            # Odd idx ptr
            p1.next = p2.next
            p1 = p1.next
            # Even idx ptr
            if p1: p2.next = p1.next
            else: p2.next = None
            p2 = p2.next
        p1 = head
        while p1.next: p1 = p1.next
        p1.next = head2

        return head