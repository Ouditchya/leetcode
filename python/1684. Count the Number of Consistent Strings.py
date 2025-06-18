class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hMap = {}
        for c in allowed: hMap[c] = 1

        ans = 0
        for word in words:
            flag = True
            for c in word:
                if not hMap.get(c, 0): 
                    flag = False
                    break
            if flag: ans += 1

        return ans