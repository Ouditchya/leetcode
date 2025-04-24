# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        # print(head)
        p1, p2 = head, head.next
        while p2 != None:
            # print(p1.val, p2.val)
            if p1.val == p2.val:
                temp = p2.next
                p1.next = temp
                p2 = temp
                # p2 = p2.next
                continue
            if p2 == None:
                break
            p1 = p1.next
            p2 = p2.next
        # print(head)
        return head