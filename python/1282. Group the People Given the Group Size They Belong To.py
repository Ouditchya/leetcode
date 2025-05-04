from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mydict = defaultdict(list)
        n = len(groupSizes)
        ans = []
        
        for i in range(n): mydict[groupSizes[i]].append(i)
        # print(mydict)

        for k, v in mydict.items():
            i, m = 0, len(v)// k
            for itr in range(m):
                temp = []
                for ctr in range(k):
                    temp.append(v[i])
                    i += 1
                ans.append(temp)

        return ans