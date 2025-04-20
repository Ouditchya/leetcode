class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]

        ls = [[1],[1,1]]

        for i in range(2, rowIndex+1):
            ls_prev = ls[i-1].copy()
            ls_new = ls[1].copy()
            len_ls_prev = len(ls[i-1])
            for j in range(1, len_ls_prev, 1):
                new_num = ls_prev[j] + ls_prev[j-1]
                ls_new.insert(j, new_num)
            ls.append(ls_new)
        
        # print(ls)

        return ls[rowIndex]
        