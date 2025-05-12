class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, np, pp = 0, 0, 0
        ls = []

        while True:
            while np < n:
                if nums[np] > 0: np += 1
                else: break
            while pp < n:
                if nums[pp] < 0: pp += 1
                else: break
            if i % 2 == 1 and np < n:
                # print("np: ", nums[np])
                ls.append(nums[np])
                np += 1
            if i % 2 == 0 and pp < n:
                # print("pp: ", nums[pp], "\n-------------------------")
                ls.append(nums[pp])
                pp += 1
            if np >= n and pp >= n: break
            i += 1

        return ls