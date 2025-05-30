class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        def getBinary(x):
            s = ''
            while x:
                d = x % 2
                s += str(d)
                x //= 2
            n = len(s)
            for i in range(n, 30): s += '0'
            return s[::-1]
        
        bin_a, bin_b, bin_c = getBinary(a), getBinary(b), getBinary(c)
        cnt = 0
        for i in range(30):
            if bin_c[i] == '0':
                if bin_a[i] == '1': cnt += 1
                if bin_b[i] == '1': cnt += 1
            if bin_c[i] == '1':
                if bin_a[i] == '0' and bin_b[i] == '0': cnt += 1

        return cnt