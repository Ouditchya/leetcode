# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p1, n = head, 0
        # Step 1: Calculate length of Linked List
        while p1 != None:
            n += 1
            p1 = p1.next
        # Step 2: If length > 2 proceed otherwise no change needed
        if n > 2:
            ls, i, m, p1 = [], 0, (n+1)//2, head
            # print(n, m, "\n")
            # Step 3: Push the 2nd half of linked list into a stack, disconnect it from the 1st half
            while p1 != None:    
                i += 1
                p0 = p1
                # if p1:
                    # print("i = ", i, " p0.val = ", p0.val, " p1.val = ", p1.val, "\n")
                    # print("ls: ", ls, "\n---------------------------------------")
                if i > m:
                    p2 = ListNode(p1.val)
                    ls.append(p2)
                p1 = p1.next
                if i == m:
                    p0.next = None
            p1, j = head, n//2-1
            # print("\nhead: ", head)
            # print("ls[0] = ", ls[0], " ls[1] = ", ls[1])
            # print("ls: ", ls, "\n------------------------------------")
            # Step 4: Rebuild the linked list as needed using the stack and updated head
            while j >= 0:
                # print("j = ", j, " ls[j] = ", ls[j], "\n head: ", head, "\n-----------------------------")
                p2 = ls[j]
                p2.next = p1.next
                p1.next = p2
                p1 = p1.next.next
                j -= 1
            # print(head)