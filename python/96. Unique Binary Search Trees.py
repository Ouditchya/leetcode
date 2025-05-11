class Solution:
    def numTrees(self, n: int) -> int:
        c = [1, 1]
        for i in range(2, 20):
            curr = 0
            # print("n = ", i)
            for j in range(i):
                curr += c[j]*c[i-j-1]
                # print(j, i-j-1, curr)
            c.append(curr)
            # print("---------------------------\n")
        return c[n]