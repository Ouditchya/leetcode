class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        f, dict_l, dict_r = 0, {}, {}

        for i in range(n):
            if dominoes[i] == 'L': f = 0
            if dominoes[i] == 'R': f = 1
            if dominoes[i] == '.' and f > 0: 
                dict_r[i] = f
                f += 1
        
        f = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L': f = 1
            if dominoes[i] == 'R': f = 0
            if dominoes[i] == '.' and f > 0: 
                dict_l[i] = f
                f += 1

        df = ''
        for i in range(n):
            if dominoes[i] == 'L' or dominoes[i] == 'R': df = df + dominoes[i]
            elif dict_l.get(i, 1000000) < dict_r.get(i, 1000000): df = df + 'L'
            elif dict_l.get(i, 1000000) > dict_r.get(i, 1000000): df = df + 'R'
            else: df = df + '.'
        
        # print(dominoes)
        # print(df)

        return df