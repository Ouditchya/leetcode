# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edge Case
        if head == None or head.next == None:
            return False
        
        # Check cycle
        p1, p2, flag = head, head, 0
        while p1.next != None or p2.next != None:
            p1 = p1.next
            p2 = p2.next.next
            if p2 == None:
                flag = 1
                break
            if p1.next == None or p2.next == None:
                flag = 1
                break
            if p1.val == p2.val and p1 == p2:
                break
        
        if flag == 1:
            return False
        else:
            return True