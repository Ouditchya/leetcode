# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1, len2 = 0, 0
        p1, p2 = l1, l2
        while p1 != None:
            len1 += 1
            p1 = p1.next
        while p2 != None:
            len2 += 1
            p2 = p2.next
        
        if len1 < len2:
            p1, p2 = l2, l1
            ans = l2
        else:
            p1, p2 = l1, l2
            ans = l1

        carry = 0
        while p1 != None:
            if p2 != None:
                y = p2.val
            else:
                y = 0
            value = p1.val + y
            new_value = (value % 10 + carry) % 10
            p1.val = new_value
            cf = lambda x: 1 if x >= 10 else 0
            carry = cf(value + carry)
            if p2 != None:
                p2 = p2.next
            if p1.next == None:
                last = p1
            p1 = p1.next

        if carry == 1:
            p3 = ListNode(1)
            last.next = p3

        print(ans)

        return ans