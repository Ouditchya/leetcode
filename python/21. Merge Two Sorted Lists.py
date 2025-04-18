# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        ls = []
        
        # Edge cases
        if p1 is None and p2 is not None:
            return p2
        elif p1 is not None and p2 is None:
            return p1
        elif p1 is None and p2 is None:
            return p1

        while p1 is not None:
            ls.append(p1.val)
            p1 = p1.next
        
        while p2 is not None:
            ls.append(p2.val)
            p2 = p2.next

        ls.sort()
        ls_len = len(ls)
        h1 = ListNode(ls[0])
        p1 = h1
        for i in range(1, ls_len, 1):
            new_node = ListNode(ls[i])
            p1.next = new_node
            p1 = p1.next
            
        # print(h1)

        return h1