class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n, C = len(A), []
        set_A, set_B = set(), set()
        for i in range(n):
            set_A.add(A[i])
            set_B.add(B[i])
            # print(set_A, set_B, set_A & set_B)
            C.append(len(set_A & set_B))
        return C