class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n, ls = len(words), []
        for i in range(n):
            if x in words[i]:
                ls.append(i)
        return ls