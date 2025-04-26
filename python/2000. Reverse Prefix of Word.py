class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        m, n = -1, len(word)

        for i in range(n):
            if word[i] == ch:
                m = i
                break

        if m == -1:
            return word
        else:
            return word[:m+1][::-1] + word[m+1:]