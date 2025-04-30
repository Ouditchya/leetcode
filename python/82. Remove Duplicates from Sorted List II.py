# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        p1, d = head, {}

        while p1 != None:
            d[p1.val] = d.get(p1.val, 0) + 1
            # print(p1.val, end = ' >')
            p1 = p1.next
        # print("\n", d, "\n------------------------------------")

        ck, cv = 0, 0
        for k, v in d.items():
            if v > 1:
                cv += 1
            ck += 1
        if ck == cv:
            return None

        while True:
            hv = head.val
            if d[hv] > 1:
                p1 = head
                while p1.val == hv and p1 != None:
                    p1 = p1.next
                head = p1
            else: break
            if head == None:
                return None

        p0, p1 = head, head.next
        while p1 != None:
            # print("1: ", p0.val, p1.val)
            if d[p1.val] > 1:
                p0.next = p1.next
                p1 = p1.next
            else:
                p0 = p0.next
                p1 = p1.next
            # if p0 and p1:
            #     print("2: ", p0.val, p1.val, "\n---------------------------")
        
        return head