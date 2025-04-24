# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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
        
        p2 = p3
        p1 = head
        while p1 != None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True