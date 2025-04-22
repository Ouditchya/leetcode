class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr, ls, ans = [0] * 101, [0] * 101, []
        
        for i in range(n):
            arr[nums[i]] += 1
        
        ls[0] = arr[0]
        for i in range(1, 101):
            ls[i] = ls[i-1] + arr[i]
        
        # print(arr)
        # print(ls)

        for i in range(n):
            if nums[i] == 0:
                ans.append(0)
            else:
                ans.append(ls[nums[i]-1])

        # print(ans)

        return ans