class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        si, sd, n = [], [], len(arr)

        # Edge case
        if n < 3: return False

        for i in range(1, n):
            cd = arr[i] - arr[i-1]
            if cd == 0: return False
            elif cd > 0: si.append(i)
            elif cd < 0: sd.append(i)

        ni, nd = len(si), len(sd)
        if ni == 0 or nd == 0: return False
        for i in range(nd):
            for j in range(ni):
                if sd[i] < si[j]: return False
        return True