class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        myset, n = set(), len(digits)
        for i in range(n):
            if digits[i] == 0: continue
            for j in range(n):
                if i == j: continue
                for k in range(n):
                    if j == k or i == k or digits[k] % 2 == 1: continue
                    myset.add(digits[i]*100 + digits[j]*10 + digits[k])
        ls = [i for i in myset]
        # ls.sort()
        return len(ls)