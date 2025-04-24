# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        p1 = head
        while p1 != None:
            p2 = ListNode()
            p2.val = p1.val
            if p1 == head:
                p2.next = None
            else:
                p2.next = p3
            p3 = p2
            p1 = p1.next

        return p3