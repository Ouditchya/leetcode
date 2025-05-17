class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n_students = len(score)
        ls, mydict = [], {}
        
        for i in range(n_students):
            mydict[score[i][k]] = i
            ls.append(score[i][k])
        ls.sort(reverse = True)

        score_sorted = []
        for i in range(n_students):
            score_sorted.append(score[mydict[ls[i]]])
        
        return score_sorted