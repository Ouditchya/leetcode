class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ls, myset, n = [], [], len(words)
        
        for i in range(n):
            myset.append(words[i])
            for j in range(i, n):
                if len(myset) == 1:
                    if groups[i] != groups[j]: myset.append(words[j])
                else: 
                    if groups[j] != groups[j-1]: myset.append(words[j])
            ls.append(myset[:])
            myset.clear()
        
        curr = 0
        for x in ls:
            if len(x) > curr:
                curr = len(x)
                myset = x
        # print(myset)
        
        return myset