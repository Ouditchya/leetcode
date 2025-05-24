# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# from collections import defaultdict

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr, n, p1 = [], 1, head
        while p1:
            arr.append(p1.val) 
            p1, n = p1.next, n+1

        # Precompute Pairs
        myset = set()
        ub = n//2
        for i in range(ub): myset.add((i, n-i-2))
        # print(myset)

        ans = 0
        for x in myset: ans = max(ans, arr[x[0]]+arr[x[1]])

        return ans