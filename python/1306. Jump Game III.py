class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [0]*n

        def solve(idx):
            nonlocal flag
            if flag: return

            if idx >= 0 and idx < n:
                if visited[idx] == 1: return
                visited[idx] = 1
                # print("idx: ", idx, " arr[idx]: ", arr[idx])
                if arr[idx] == 0: 
                    flag = True
                    return
                solve(idx+arr[idx])
                solve(idx-arr[idx])

        flag = False
        solve(start)

        return flag