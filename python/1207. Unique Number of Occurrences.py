class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h1, h2 = {}, {}
        for num in arr: h1[num] = h1.get(num, 0) + 1
        for v in h1.values(): 
            h2[v] = h2.get(v, 0) + 1
            if h2[v] > 1: return False
        return True