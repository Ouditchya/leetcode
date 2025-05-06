class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        op, n = [], len(queries)

        # Construct permutation
        for i in range(m):
            p0 = ListNode(i+1)
            if i == 0: p1, head = p0, p0
            else:
                p1.next = p0
                p1 = p0
        
        # Check list
        # p1 = head
        # while p1:
        #     print(p1.val, end = " ")
        #     p1 = p1.next

        for i in range(n):
            pos, f, val = 0, 0, queries[i]
            p0, p1 = head, head
            if head.val == val: op.append(0)
            else:
                while p1 or f == 0:
                    if p1.val == val:
                        p0.next = p1.next
                        p1.next = head
                        head = p1
                        f = 1
                        op.append(pos)
                    pos += 1
                    p0 = p1
                    p1 = p1.next

        return op