class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        lb, ub = max(sum(weights)// days, max(weights)), sum(weights)

        def simulate(capacity):
            # ans, ls = [], []
            currSum, time = 0, 0
            for i in range(n):
                # print("capacity: ", capacity, " currSum: ", currSum, " weights[i]: ", weights[i], " time: ", time)
                # print("ls: ", ls, " ans: ", ans, "\n-------------------------------")
                if currSum + weights[i] > capacity:
                    currSum, time = weights[i], time + 1
                    # ans.append(ls[:])
                    # ls.clear()
                    # ls.append(weights[i])
                else:
                    currSum += weights[i]
                    # ls.append(weights[i])
            # ans.append(ls[:])
            # print(ans)
            return time+1

        def binarySearch(l, r):
            while l <= r:
                m = (l + r) // 2
                time = simulate(m)
                # if time == days: return m
                if time > days: l = m + 1
                else: r = m - 1
            return l

        minCapacity = binarySearch(lb, ub)
        # for i in range(lb, ub):
        #     time = simulate(i)
        #     if time == days: 
        #         minCapacity = i
        #         break

        return minCapacity