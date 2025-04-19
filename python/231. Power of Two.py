class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        elif n == 1:
            return True

        ls = [1]
        for i in range(1, 31, 1):
            ls.append(2*ls[i-1])
            if n == ls[i]:
                return True
        
        return False