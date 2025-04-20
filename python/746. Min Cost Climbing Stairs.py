class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        if len_cost == 1:
            return 0

        min_cost = [0, 0]

        for i in range(2, len_cost+1, 1):
            # print(i, i-1, i-2)
            min_cost.append(min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2]))

        # print(min_cost)

        return min_cost[len_cost] 