class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats.sort()
        students.sort()
        s = 0
        for i in range(n):
            s += abs(students[i] - seats[i])
        # print(seats)
        # print(students)
        return s