class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt, n = 0, len(pref)
        for word in words:
            if len(word) >= n and word[:n] == pref: cnt += 1
        return cnt 