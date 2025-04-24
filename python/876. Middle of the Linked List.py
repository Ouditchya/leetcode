# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        p1, ctr = head, 1
        while p1 != None:
            ctr += 1
            p1 = p1.next
        if ctr % 2 == 0:
            mid = ctr/2
        else:
            mid = ctr//2 + 1
        p1, itr = head, 1
        while itr < mid:
            itr += 1
            p1 = p1.next
        return p1