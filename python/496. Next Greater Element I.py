class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        monoStack, idx = [], [-1]*m

        top = -1
        for i in range(m-1, -1, -1):
            # If monotonic stack is empty, push current element
            if top == -1: 
                monoStack.append(nums2[i])
                top += 1
            # If monotonic stack is not empty + current element < top of stack
            elif nums2[i] < monoStack[top]:
                idx[i] = monoStack[top]
                monoStack.append(nums2[i])
                top += 1
            # If monotonic stack is not empty + current element > top of stack
            else:
                while(monoStack[top] < nums2[i]): 
                    monoStack.pop()
                    top -= 1
                    if top < 0: break
                # monotonic stack is not empty, update idx
                if top != -1: idx[i] = monoStack[top]
                monoStack.append(nums2[i])
                top += 1

        nge = {}
        for i in range(m): nge[nums2[i]] = idx[i]
        # print(nge)

        ans = []
        for i in range(n): ans.append(nge[nums1[i]])

        return ans