class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ls = [0] * n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if boxes[j] == '1':
                    ls[i] += abs(j - i)
        return ls