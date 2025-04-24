# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge case
        if head == None or head.next == None or left == right:
            return head
        
        p1, ctr = head, 1
        while p1 != None:
            # start reverse
            if ctr == left:
                p2 = ListNode()
                p2.val = p1.val
                p2.next = None
                p3 = p2
                p4 = p2
            # continue reverse
            elif ctr >= left:
                p2 = ListNode()
                p2.val = p1.val
                p2.next = p3
                p3 = p2
            # end reverse
            ctr += 1
            p1 = p1.next
            if ctr > right:
                break

        # print(p3)

        p1, ctr = head, 1
        while ctr < right:
            p1 = p1.next
            ctr += 1
        p4.next = p1.next

        # print(p3)

        if left == 1:
            return p3

        p1, ctr = head, 1
        while ctr < left:
            p2 = p1
            p1 = p1.next
            ctr += 1
        p2.next = p3

        return head