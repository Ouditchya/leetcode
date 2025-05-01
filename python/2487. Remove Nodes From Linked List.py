# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return head
        
        ls = []
        
        def rmv(node, max_val = 0) -> int:
            if node.next == None: 
                ls.append(node.val)
                return node.val
            next_val = rmv(node.next, max_val)
            max_val = max(max_val, node.val, next_val)
            if node.val >= max_val:
                ls.append(node.val)
            return max_val
        
        rmv(head, 0)
        n = len(ls)
        new_head = ListNode(ls[n-1])
        p0 = new_head
        for i in range(n-2, -1, -1):
            p1 = ListNode(ls[i])
            if not head.next:
                new_head.next = p1
                p0 = new_head
            else:
                p0.next = p1
                p0 = p0.next
            p1 = p1.next
        
        return new_head    