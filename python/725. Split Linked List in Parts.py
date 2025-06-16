# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        p1, ls = head, []
        while p1: 
            ls.append(p1.val)
            p1 = p1.next
        # print("ls: ", ls)
        num = len(ls)// k
        rem = len(ls) - num*k
        # print("num: ", num, " rem: ", rem)
        
        itr, arr = 0, []
        for i in range(k):
            temp = []
            if i < rem:
                for j in range(num+1): temp.append(ls[itr+j])
                itr += (num+1)
            else:
                for j in range(num): temp.append(ls[itr+j])
                itr += num
            arr.append(temp)    
        # print("arr: ", arr)

        def makeLinkedList(ls):
            if len(ls) == 0: return None
            h1 = ListNode(ls[0])
            p1 = h1
            for x in range(1, len(ls)): 
                newNode = ListNode(ls[x])
                p1.next = newNode
                p1 = newNode
            return h1
        
        ans = []
        for i in range(k): ans.append(makeLinkedList(arr[i]))

        return ans