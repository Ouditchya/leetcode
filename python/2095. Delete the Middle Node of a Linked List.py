# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None: return None
        
        p1, p2 = head, head
        while p2:
            if p2.next is None: break
            p2 = p2.next.next
            prev = p1
            p1 = p1.next
        prev.next = p1.next

        return head