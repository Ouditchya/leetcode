# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        p1, ctr = head, 1
        while True:
            if p1.next == None:
                break
            elif ctr == 1:
                temp = p1.next
                p1.next = p1.next.next
                temp.next = p1
                new_head = temp
                ctr += 1
            elif p1.next.next == None:
                break
            else:
                p0 = p1
                p1 = p1.next
                temp = p1.next
                p0.next = temp
                p1.next = temp.next
                temp.next = p1
                ctr += 1
            # print(new_head)

        return new_head