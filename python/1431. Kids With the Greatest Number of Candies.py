class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        currMax = candies[0]
        for candy in candies: currMax = max(currMax, candy)

        ans = []
        for candy in candies: ans.append(candy+extraCandies>=currMax)

        return ans