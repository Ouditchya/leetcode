class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n, m = len(s), len(s)//2
        for i in range(n):
            if i == m:
                break
            temp = s[i]
            # print(temp, s[i], s[n-i-1])
            s[i] = s[n-i-1]
            s[n-i-1] = temp
            # print(temp, s[i], s[n-i-1], "\n------------------------")