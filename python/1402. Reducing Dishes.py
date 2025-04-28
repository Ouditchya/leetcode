class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()

        if satisfaction[n-1] <= 0:
            return 0

        # print(satisfaction)
        max_val = -1000000000
        for i in range(n-1, -1, -1):
            curr_val, idx = 0, 1
            for j in range(i, n, 1):
                curr_val += (idx*satisfaction[j])
                idx += 1
            # print(curr_val)
            if curr_val < max_val:
                break
            max_val = max(max_val, curr_val)

        return max_val