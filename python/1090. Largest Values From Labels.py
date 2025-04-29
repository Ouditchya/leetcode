class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n, d1, d2, itr, ans = len(values), {}, {}, 0, 0
        for i in range(n):
            d1[values[i]] = []

        for i in range(n):
            d1[values[i]].append(labels[i])
            d2[labels[i]] = 0
        # print(d1)
        # print(d2)

        values.sort()
        # print("--------------------------------\n",values,"\n--------------------------------")
        for i in range(n-1, -1, -1):
            curr_value = values[i]
            curr_label = d1[curr_value][0]
            if d2.get(curr_label, 0) == useLimit:
                d1[curr_value].remove(curr_label)
                continue
            else:
                d2[curr_label] += 1
                itr += 1
                ans += curr_value
                d1[curr_value].remove(curr_label)
            if itr == numWanted:
                break
        # print(d1)
        # print(d2)
        
        return ans