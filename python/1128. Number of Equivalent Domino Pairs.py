class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mydict, n, pairs = {}, len(dominoes), 0
        for i in range(n):
            a, b = min(dominoes[i][0], dominoes[i][1]), max(dominoes[i][0], dominoes[i][1])
            mydict[(a, b)] = mydict.get((a, b), 0) + 1
        # print(mydict)
        for v in mydict.values():
            if v == 1: continue
            else: pairs += (v*(v-1))//2
        return pairs