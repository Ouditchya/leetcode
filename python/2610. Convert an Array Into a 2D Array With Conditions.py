class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hmap = {}
        for num in nums: hmap[num] = hmap.get(num, 0) + 1

        ans = []
        while True:
            ls = []
            if not hmap: break
            for k in hmap.keys():
                if hmap[k] > 0:
                    ls.append(k)
                    hmap[k] -= 1
                if not hmap.get(k, 0): del hmap[k]
            ans.append(ls)
        
        return ans