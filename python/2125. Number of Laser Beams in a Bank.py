class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        cnt = []
        for row in bank:
            lasers = 0
            for cell in row:
                if cell == "1": lasers += 1
            if lasers > 0: cnt.append(lasers)
        
        ans = 0
        for i in range(1, len(cnt)): ans += cnt[i]*cnt[i-1]

        return ans