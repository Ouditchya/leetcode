class Solution:
    def defangIPaddr(self, address: str) -> str:
        n = len(address)
        str1 = ''
        for i in range(n):
            if address[i] == '.':
                str1 += '[.]'
            else:
                str1 += address[i]
        return str1