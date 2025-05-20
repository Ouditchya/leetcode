class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]

        if (a + b <= c) or (a + c <= b) or (b + c <= a): return "none"
        elif a == b and b == c: return "equilateral"
        elif (a == b and a != c) or (a == c and a != b) or (b == c and a != c): return "isosceles"
        elif (a != b and b != c) and (a + b > c) and (b + c > a) and (a + c > b): return "scalene"
        else: return "none"