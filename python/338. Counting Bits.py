class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        
        ans = [0, 1]
        for i in range(2, n+1, 1):
            bits = 0
            num = i
            while num > 0:
                if num % 2 != 0:
                    bits += 1
                num = num >> 1
            ans.append(bits)
        
        return ans